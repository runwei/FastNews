(function($) {

	$.fn.scrollPagination = function(options) {
		
		var settings = { 
			nop     : 6, // The number of posts per scroll to be loaded
			offset  : 0, // Initial offset, begins at 0 in this case
			error   : 'No More Posts!', // When the user reaches the end this is the message that is
			                            // displayed. You can change this if you want.
			delay   : 100, // When you scroll down the posts will load after a delayed amount of time.
			               // This is mainly for usability concerns. You can alter this as you see fit
			scroll  : true, // The main bit, if set to false posts will not load as the user scrolls. 
			               // but will still load if the user clicks.
			description : 'index',
		}
		
		// Extend the options so they work with the plugin
		if(options) {
			$.extend(settings, options);
		}
		
		// For each so that we keep chainability.
		return this.each(function() {		
			
			// Some variables 
			$this = $(this);
			$settings = settings;
			var offset = $settings.offset;
			var busy = false; // Checks if the scroll action is happening 
			                  // so we don't run it multiple times
			
			// Custom messages based on settings
			if($settings.scroll == true) $initmessage = 'Scroll for more or click here';
			else $initmessage = 'Click for more';
			
			// Append custom messages and extra UI
			$this.append('<div id="toappend"></div><div class="loading-bar">'+$initmessage+'</div>');
			function getData() {
				// Post data to ajax.php
				
			    $.ajax({
			        url: "/get_data/", 
					method: "POST",
					data: {
				    	number: $settings.nop,
				    	offset: offset,
				    	desc:  $settings.description,
					},
			        crossDomain: false
			    })
				.done(function(data) {	
					$this.find('.loading-bar').html($initmessage);
					    offset = offset+$settings.nop;
						$this.find('#toappend').append(data);
				});
				
				// $.post('/get_data/', {
				//     number: $settings.nop,
				//     offset: offset,
				// }, function(data) {
				// 	$this.find('.loading-bar').html($initmessage);
				// 	    offset = offset+$settings.nop;
				// 		$this.find('#toappend').append(data);
				// });
			}
			// getData(); // Run function initially
			$(window).scroll(function() {
				// Check the user is at the bottom of the element
				if($(window).scrollTop() + $(window).height() >= $(document).height()) {
					getData();
				}		
			});
			
			// Also content can be loaded by clicking the loading bar/
			$this.find('.loading-bar').click(function() {
			
				if(busy == false) {
					busy = true;
					getData();
				}
			
			});
			
		});
	}

})(jQuery);
