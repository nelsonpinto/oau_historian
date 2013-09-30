
var display_msg = function(msg, elem) {
	var msg_div = $('<div class="error_msg"><p>'+msg+'</p></div>');
	msg_div.insertAfter(elem).fadeIn('slow').animate({opacity: 1.0}, 5000).fadeOut('slow',function() { msg_div.remove(); });
};

var table_hide = function(elem) {
	//elem.slideUp(1000).fadeIn(400);
	elem.toggle("slow");
};

var msg_alert = function(elem) {
	alert("Thanks for visiting!.$(elem)");
};

var show_obj = function(elem) {
	alert("Thanks for vi!.$(elem)");
};