import re

from opendevin.controller.action_parser import ActionParser, ResponseParser
from opendevin.events.action import (
    Action,
    AgentDelegateAction,
    AgentFinishAction,
    CmdRunAction,
    IPythonRunCellAction,
    MessageAction,
    BrowseInteractiveAction
)
from opendevin.core.logger import opendevin_logger as logger
import ast


class InterleavingResponseParser(ResponseParser):
    """
    Parser action:
        - CmdRunAction(command) - bash command to run
        - IPythonRunCellAction(code) - IPython code to run
        - AgentDelegateAction(agent, inputs) - delegate action for (sub)task
        - MessageAction(content) - Message action to run (e.g. ask for clarification)
        - AgentFinishAction() - end the interaction
    """

    def __init__(
        self,
    ):
        # Need pay attention to the item order in self.action_parsers
        self.action_parsers = [
            InterleavingActionParserFinish(),
            InterleavingActionParserCmdRun(),
            InterleavingActionParserIPythonRunCell(),
            InterleavingActionParserBrowse(),
        ]
        self.default_parser = InterleavingActionParserMessage()

    def parse(self, response: str) -> Action:
        action_str = self.parse_response(response)
        return self.parse_action(action_str)

    def parse_response(self, response) -> str:
        if isinstance(response, str): action = response
        else: action = response.choices[0].message.content
        for lang in ['bash', 'ipython', 'browse']:
            if f'<execute_{lang}>' in action and f'</execute_{lang}>' not in action:
                action += f'</execute_{lang}>'
        return action

    def parse_action(self, action_str: str) -> Action:
        for action_parser in self.action_parsers:
            if action_parser.check_condition(action_str):
                return action_parser.parse(action_str)
        return self.default_parser.parse(action_str)


class InterleavingActionParserFinish(ActionParser):
    """
    Parser action:
        - AgentFinishAction() - end the interaction
    """

    def __init__(
        self,
    ):
        self.finish_command = None

    def check_condition(self, action_str: str) -> bool:
        self.finish_command = re.search(r'<finish>.*</finish>', action_str, re.DOTALL)
        return self.finish_command is not None

    def parse(self, action_str: str) -> Action:
        assert (
            self.finish_command is not None
        ), 'self.finish_command should not be None when parse is called'
        thought = action_str.replace(self.finish_command.group(0), '').strip()
        return AgentFinishAction(thought=thought)


class InterleavingActionParserCmdRun(ActionParser):
    """
    Parser action:
        - CmdRunAction(command) - bash command to run
        - AgentFinishAction() - end the interaction
    """

    def __init__(
        self,
    ):
        self.bash_command = None

    def check_condition(self, action_str: str) -> bool:
        self.bash_command = re.search(
            r'<execute_bash>(.*?)</execute_bash>', action_str, re.DOTALL
        )
        return self.bash_command is not None

    def parse(self, action_str: str) -> Action:
        assert (
            self.bash_command is not None
        ), 'self.bash_command should not be None when parse is called'
        thought = action_str.replace(self.bash_command.group(0), '').strip()
        # a command was found
        command_group = self.bash_command.group(1).strip()
        if command_group.strip() == 'exit':
            return AgentFinishAction()
        return CmdRunAction(command=command_group, thought=thought)


class InterleavingActionParserIPythonRunCell(ActionParser):
    """
    Parser action:
        - IPythonRunCellAction(code) - IPython code to run
    """

    def __init__(
        self,
    ):
        self.python_code = None
        self.act_python_code = None
        self.jupyter_kernel_init_code: str = 'from agentskills import *'

    def check_condition(self, action_str: str) -> bool:
        # Check for traditional <execute_ipython> format
        self.python_code = re.search(
            r'<execute_ipython>(.*?)</execute_ipython>', action_str, re.DOTALL
        )
        
        # Check for the new explicit format: "act - IPythonRunCellAction"
        if not self.python_code:
            self.act_python_code = re.search(
                r'act - IPythonRunCellAction\s+CODE:\s*(.*?)(?=\n\n|$)', 
                action_str, 
                re.DOTALL
            )
            return self.act_python_code is not None
            
        return self.python_code is not None

    def parse(self, action_str: str) -> Action:
        thought = ""
        code_group = ""
        
        if self.python_code:
            assert (
                self.python_code is not None
            ), 'self.python_code should not be None when parse is called'
            code_group = self.python_code.group(1).strip()
            thought = action_str.replace(self.python_code.group(0), '').strip()
        elif self.act_python_code:
            assert (
                self.act_python_code is not None
            ), 'self.act_python_code should not be None when parse is called'
            code_group = self.act_python_code.group(1).strip()
            # Extract thought before the "act - IPythonRunCellAction" part
            act_match = re.search(r'(.*?)act - IPythonRunCellAction', action_str, re.DOTALL)
            if act_match:
                thought = act_match.group(1).strip()
            else:
                thought = ""
            
            logger.info(f"Parsed IPythonRunCellAction with new format. Code length: {len(code_group)}")
        
        return IPythonRunCellAction(
            code=code_group,
            thought=thought,
            kernel_init_code=self.jupyter_kernel_init_code,
        )


class InterleavingActionParserMessage(ActionParser):
    """
    Parser action:
        - MessageAction(content) - Message action to run (e.g. ask for clarification)
    """

    def __init__(
        self,
    ):
        pass

    def check_condition(self, action_str: str) -> bool:
        # We assume the LLM is GOOD enough that when it returns pure natural language
        # it wants to talk to the user
        return True

    def parse(self, action_str: str) -> Action:
        # Check if this message appears to contain Python code that should be in IPythonRunCellAction
        python_code_indicators = [
            "```python",
            "```execute_ipython",
            "from utils import",
            "list_tools(site=",
            "call_function(",
            "get_documentation(",
            "import "
        ]
        
        contains_python = any(indicator in action_str for indicator in python_code_indicators)
        if contains_python:
            logger.warning(f"MessageAction contains what appears to be Python code. Consider using IPythonRunCellAction instead. Content: {action_str[:200]}...")
            
            # If message contains both "act - IPythonRunCellAction" and "CODE:" patterns, try to extract and execute the code
            if "act - IPythonRunCellAction" in action_str and "CODE:" in action_str:
                logger.info("Converting incorrect MessageAction to IPythonRunCellAction")
                # Try to extract code
                act_python_code = re.search(
                    r'act - IPythonRunCellAction\s+CODE:\s*(.*?)(?=\n\n|$)', 
                    action_str, 
                    re.DOTALL
                )
                if act_python_code:
                    code_group = act_python_code.group(1).strip()
                    # Extract thought before the "act - IPythonRunCellAction" part
                    act_match = re.search(r'(.*?)act - IPythonRunCellAction', action_str, re.DOTALL)
                    thought = act_match.group(1).strip() if act_match else ""
                    
                    logger.info(f"Successfully converted MessageAction to IPythonRunCellAction, code length: {len(code_group)}")
                    from opendevin.events.action import IPythonRunCellAction
                    return IPythonRunCellAction(
                        code=code_group,
                        thought=thought,
                    )
            
        return MessageAction(content=action_str, wait_for_response=True)


class InterleavingActionParserBrowse(ActionParser):
    """
    Parser action:
        - browse_action - browse
    """

    def __init__(
        self,
    ):
        self.agent_browse = None

    def check_condition(self, action_str: str) -> bool:
        self.agent_browse = re.search(
            r'<execute_browse>(.*)</execute_browse>', action_str, re.DOTALL
        )
        return self.agent_browse is not None

    def parse(self, action_str: str) -> Action:
        assert (
            self.agent_browse is not None
        ), 'self.agent_browse should not be None when parse is called'
        #thought = action_str.replace(self.agent_browse.group(0), '').strip()
        browse_actions = self.agent_browse.group(1).strip()
        response_parser = BrowsingResponseParser()
        return response_parser.parse(browse_actions)

class BrowsingResponseParser(ResponseParser):
    def __init__(
        self,
    ):
        # Need to pay attention to the item order in self.action_parsers
        self.action_parsers = [BrowsingActionParserMessage()]
        self.default_parser = BrowsingActionParserBrowseInteractive()

    def parse(self, response: str) -> Action:
        action_str = self.parse_response(response)
        return self.parse_action(action_str)

    def parse_response(self, response) -> str:
        action_str = response.strip()
        if action_str.count('```') > 2 and action_str.startswith('```') and action_str.endswith('```'): action_str = action_str.replace('```', '')
        if not action_str.endswith('```'):
            action_str = action_str + '```'
        if not action_str.startswith('```'):
            action_str = '```' + action_str
        return action_str

    def parse_action(self, action_str: str) -> Action:
        for action_parser in self.action_parsers:
            if action_parser.check_condition(action_str):
                return action_parser.parse(action_str)
        return self.default_parser.parse(action_str)


class BrowsingActionParserMessage(ActionParser):
    """
    Parser action:
        - BrowseInteractiveAction(browser_actions) - unexpected response format, message back to user
    """

    def __init__(
        self,
    ):
        pass

    def check_condition(self, action_str: str) -> bool:
        return '```' not in action_str

    def parse(self, action_str: str) -> Action:
        msg = f'send_msg_to_user("""{action_str}""")'
        return BrowseInteractiveAction(
            browser_actions=msg,
            thought=action_str,
            browsergym_send_msg_to_user=action_str,
        )


class BrowsingActionParserBrowseInteractive(ActionParser):
    """
    Parser action:
        - BrowseInteractiveAction(browser_actions) - handle send message to user function call in BrowserGym
    """

    def __init__(
        self,
    ):
        pass

    def check_condition(self, action_str: str) -> bool:
        return True

    def parse(self, action_str: str) -> Action:
        thought = action_str.split('```')[0].strip()
        action_str = action_str.split('```')[1].strip()
        msg_content = ''
        for sub_action in action_str.split('\n'):
            if 'send_msg_to_user(' in sub_action:
                tree = ast.parse(sub_action)
                args = tree.body[0].value.args  # type: ignore
                msg_content = args[0].value

        return BrowseInteractiveAction(
            browser_actions=action_str,
            thought=thought,
            browsergym_send_msg_to_user=msg_content,
        )
