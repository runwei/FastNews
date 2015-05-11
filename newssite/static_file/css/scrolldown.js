$(document).ready(function(){
	$('#id-btn-next').click( function() {
		get_data(0,6);//$('#test').val()  from form
	});	
	$('#toappend').scrollPagination({

		nop     : 6, // The number of posts per scroll to be loaded
		offset  : 6, // Initial offset, begins at 0 in this case
		error   : 'No More Posts!', // When the user reaches the end this is the message that is
		                            // displayed. You can change this if you want.
		delay   : 100, // When you scroll down the posts will load after a delayed amount of time.
		               // This is mainly for usability concerns. You can alter this as you see fit
		scroll  : true, // The main bit, if set to false posts will not load as the user scrolls. 
		               // but will still load if the user clicks.
		description : $('meta[name=description]').attr("content")
	});
	
});

function get_data(index,number) {
	// $("#test1").show();

	$.ajax({
	    type: 'POST',
	    url: '/get_data/',
	    data: {foo: 'bar'},
	    dataType: 'json'
	})
	.done(function(response) {
		alert(response['result'])
	    // $("#test2").show();
	})
	.fail(function() {
	    $("#test1").show();
	});
};

