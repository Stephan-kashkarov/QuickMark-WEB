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
			dataType: "json",
			data: {
				username: $(".login-user").val(),
				password: $(".login-pass").val(),
				remember: $(".login-chck").val(),
			},
			success: function (msg) {
				console.log("Hello!");
				
				
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
})