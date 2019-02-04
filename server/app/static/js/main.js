// See https://github.com/daneden/animate.css




$(document).ready(function(){
	$(".di").hover(function () {
		$(this).css("font-size", "22.5px");
		$(this).css("color", "#e5e5e5");
		$(this).css("border-bottom", "3px solid ");
	}, function () {
		$(this).css("font-size", "22px");
		$(this).css("color", "black");
		$(this).css("border-bottom", "3px solid red");
	});
});
	
	
$.fn.extend({
	animateCss: function (animationName, callback) {
		var animationEnd = (function (el) {
			var animations = {
				animation: 'animationend',
				OAnimation: 'oAnimationEnd',
				MozAnimation: 'mozAnimationEnd',
				WebkitAnimation: 'webkitAnimationEnd',
			};

			for (var t in animations) {
				if (el.style[t] !== undefined) {
					return animations[t];
				}
			}
		})(document.createElement('div'));

		$(this).addClass('animated ' + animationName).one(animationEnd, function () {
			$(this).removeClass('animated ' + animationName);

			if (typeof callback === 'function') callback();
		});

		return this;
	},
});

$(function(){
	$("#logout").on('click', (e) => {
		e.preventDefault()
		$.ajax({
			url:"/api/auth/logout",
			type: "POST",
		}).then(() => {
			window.location.reload()
		})
	})
})



