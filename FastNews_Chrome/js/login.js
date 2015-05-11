$(document).ready(function(){

   // jQuery methods go here...
	$('#redirect').click( function() {
		window.open("http://52.10.183.132/index.html");
	});
	$('#submit').click( function() {
	    //e.preventDefault();
		$("#test1").text($('#email').val());
		$("#test1").show();
		if ($('#email').val()=='11')
		window.location.href='today_pick.html';
		else alert("bad credentials") 
	});
	
});