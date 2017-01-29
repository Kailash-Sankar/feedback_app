	/* 
	handle cliks on nav bar and side bar.
	$('.mdl-navigation__link, .mdl-layout-title').click( function(e) {
		//e.preventDefault();
		var ele = $(this).attr('href');
		handle_hash_change(ele);
	});
	*/
	
	//On page load, redirect user to the #hash slide if any
	$(document).ready( function() {
		var hash = window.location.hash.split('#')[1];
		console.log('Page load hash changed : ', hash );
		if( hash ){
			hash = '#' + hash;
			handle_hash_change(hash);	
		}	
	});	
	
	//for cross browser testing.
	if ("onhashchange" in window) {
    console.log("The browser supports the hashchange event!");
	}
	//handle URL
	function locationHashChanged() {
		console.log('hash change event triggered');
		if (location.hash) {
			handle_hash_change(location.hash);
		}
		else {
			//default redirect user to #slide-search
			handle_hash_change('#slide-home');
		}
	}
	//attach event
	window.onhashchange = locationHashChanged;
	
		
	// Take user to #hash slide
	function handle_hash_change(ele) {
		
		console.log('Element id',ele);
	
		//show slected slide
		$(".goc-home-text-container").fadeOut('slow');
		
		if( ele == '#slide-home' ) {
			//something special for home.
		}
		else {
			$(ele).slideDown(800);
		}
		
		//to close the drawer
		$('.mdl-layout__drawer').removeClass('is-visible');		
	}
	
	/* Show or hide background -- not used.
	function show_hide_bg(ele) {
		if( ele == '#slide-search') {
			$(".mdl-layout").removeClass('hide-bg');
		}
		else {
			$(".mdl-layout").addClass('hide-bg');
		}
	}
	*/
