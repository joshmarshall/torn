
var init = function() {
	var details = $("li p.detail");
	details.hide();
	var titles = $('li p.title');
	titles.click(function(e) {
		var me = $($(this).parent().find("p.detail"));
		if (!me.data('visible')) {
			me.data('visible', true);
			me.slideDown(200);
		} else {
			me.data('visible', false);
			me.slideUp(200);
		}
	});
};

$(init)
