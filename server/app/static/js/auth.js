$(function(){
	$(".steph-register").hide()


	$(".nav-link").on('click', function (e) {
		e.preventDefault()
		$(".active").removeClass("active")
		$(this).addClass("active")

		var tab = $(this).text()
		switch (tab) {
			case "Login":
				$(".steph-register").hide()
				$(".steph-login").show()
				break;

			case "Register":
				$(".steph-login").hide()
				$(".steph-register").show()
				break;

			default:
				break;
		}
	})

	$(".login-btn").on("click", function (e) {
		e.preventDefault()
		$.ajax({
			type: "POST",
			url: "/api/auth/login",
			dataType: "application/json",
			data: {
				username: $(".login-user").val(),
				password: $(".login-pass").val(),
				remember: $(".login-chck").val(),
			},
		}).fail(function (resp) {
			if (resp.status == 200) {
				$.notify({
					message: resp.responseText,
				}, {
					type: 'danger',
					animate: {
						enter: 'animated fadeInDown',
						exit: 'animated fadeOutUp'
					},
					allow_dismiss: true,
				})
			} else if (resp.status == 201){
				$.notify({
					title: 'Login | ',
					message: "Succeeded",
				}, {
					type: 'success',
					animate: {
						enter: 'animated fadeInDown',
						exit: 'animated fadeOutUp'
					},
					allow_dismiss: true,
				})
			}
		})
	})

	$(".register-btn").on('click', function(e){
		e.preventDefault()
		
		$.ajax({
			type: "POST",
			url: "/api/auth/register",
			dataType: "application/json",
			data: {
				username: $(".register-username").val(),
				password: $(".register-password").val(),
				email: $(".register-email").val(),
			},
		}).fail(function(resp){
			$.notify({
				message: resp.responseText,
			},{
				type: "info",
				animate: {
						enter: 'animated fadeInDown',
						exit: 'animated fadeOutUp'
					},
					allow_dismiss: true,
			})
		})
	})
})