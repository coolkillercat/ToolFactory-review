# TODOs
## Improve Tool refinement code
Current code only tests the parameters, we need to
1. Update tools with verified parameters
2. Make the tool db accessibile to the agent
## COMPARE WITH OTHER WEBAGENTS
Hybrid Agent(https://github.com/yueqis/API-Based-Agent)
SkillWeaver(https://github.com/OSU-NLP-Group/SkillWeaver) (less important different; research question)
1. Connect our (refined) tools with their agent(They both use the base agent CodeAct, which allows web browsing as well)
2. Test on WebArena benchmark
3. Show our results in: 
agent+generated tools
agent+generated tools+validation
agent+generated tools+validation+refinement