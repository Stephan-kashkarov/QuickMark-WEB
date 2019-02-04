// See https://github.com/daneden/animate.css




$(document).ready(function(){
	$(".di").hover(function () {
		$(this).css("border-bottom", "2px solid red");
		$(this).css("color", "grey");
	}, function () {
		$(this).css("border-bottom", "1px solid red");
		$(this).css("color", "black");
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



