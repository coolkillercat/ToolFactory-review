jQuery(function($){ // wait while jQuery loads (document-ready)

	$('input#submit').addClass('btn btn-primary'); // add styles for submit button in comments

	$('table#wp-calendar').addClass('table table-condensed'); // add styles for calendar

	$('.search-submit-button').click(function() { // submit the form if the search icon was clicked
		$(this).closest('form').submit();
	});

	$('input[type=submit], input[type=image], input[type=button], input[type=reset], button').addClass('btn').addClass('btn-default');

	// fix when long fixed menu overlaps site content
	var window_width = $(window).width();
	if( window_width > 979 ) {
		var menu_height = $('.navbar-fixed-top').height();
		if( menu_height > 50 ) { // if there are more than one row of menu items
			$('.site-content-pusher').css( 'height', menu_height+'px' );
		}
	} else { // narrow screen size
		$('.site-content-pusher').css( 'height', '0px' ); // remove height property for pusher because top menu is not fixed when less then 979px
	}

});


jQuery(window).bind( 'resize', function() { // fix when long fixed menu overlaps site content on resize
	var window_width = jQuery(window).width();
	if( window_width > 979 ) {
		var menu_height = jQuery('.navbar-fixed-top').height();
		if( menu_height > 50 ) { // if there are more than one row of menu items
			jQuery('.site-content-pusher').css( 'height', menu_height+'px' );
		} else {
			jQuery('.site-content-pusher').css( 'height', '' ); // remove height property for pusher when menu has only 1 row
		}
	} else { // narrow screen size
		jQuery('.site-content-pusher').css( 'height', '0px' ); // remove height property for pusher because top menu is not fixed when less then 979px
	}
});
