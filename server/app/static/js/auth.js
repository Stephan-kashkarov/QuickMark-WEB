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
		jsonData = JSON.stringify({
			username: $("#login-user").val(),
			password: $("#login-pass").val(),
			remember: !($("#login-chck").val()),
		})
		
		$.ajax({
			type: "POST",
			url: "/api/auth/login",
			contentType: 'application/json;charset=UTF-8',
			dataType: 'jsonp',
			data: jsonData,
		}).fail(function (resp) {
			if (resp.status != 201) {
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
			} else {
				window.location.pathname = "/dash"
			}
		})
	})

	$(".register-btn").on('click', function(e){
		e.preventDefault()
		jsonData = JSON.stringify({
			"username": $("#register-username").val(),
			"password": $("#register-password").val(),
			"email": $("#register-email").val(),
		})
		$.ajax({
			type: "POST",
			url: "/api/auth/register",
			contentType: 'application/json;charset=UTF-8',
			dataType: 'jsonp',
			data: jsonData,
		}).fail(function(resp){
			console.log(resp.status, resp);
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
			if (resp.status == 201){
				setTimeout(5000, window.location.reload)
			}
		})
	})
})