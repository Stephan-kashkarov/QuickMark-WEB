$(function(){
	$(".steph-register").hide()


	$(".nav-link").on('click', function (e) {
		e.preventDefault()
		$(".active").removeClass("active")
		$(this).addClass("active")

		let tab = $(this).text()
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

	$(".login-btn").on("click", async function (e) {
		e.preventDefault()
		let resp = $.ajax({
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
			console.log("Hello!")
			console.log(resp.status, resp.responseText)
			if (resp.status == 200) {
				$.notify({
					title: 'Login',
					messege: resp.responseText,
				}, {
					type: 'info',
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