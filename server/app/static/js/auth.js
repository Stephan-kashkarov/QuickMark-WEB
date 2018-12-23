$(function(){
	$(".register-form").hide()
	$(".nav-tabs .nav-item").on('click', function (e) {
		e.preventDefault()
		if (!($(this).hasClass("active"))){
			$(".nav-tabs .active").removeClass("active")
			$(this).addClass("active")
			switch ($(this).text()) {

				case "Login":

					$(".register-form").animateCss("bounceOutRight", function () {
						$(".register-form").hide()
						$(".login-form").show()
						$(".login-form").animateCss("bounceInLeft")
					})
					break
				
				case "Register":
					$(".login-form").animateCss("bounceOutLeft", function () {
						$(".login-form").hide()
						$(".register-form").show()
						$(".register-form").animateCss("bounceInRight")
					})
					break
				
				default:
					break
			}
		}
	})

	$(".login-submit").on('click', async (e) => {
		e.preventDefault()
		formData = {
			"type": "login",
			'username': $("#username").val(),
			'passowrd': $("#password").val(),
			"remember": $("#remember").val()
		}
		$.ajax({
			url: window.location,
			method: "POST",
			data: JSON.stringify(formData),
			contentType: "application/json charset=utf-8",
			dataType: "json"
		}).fail((err) => { // Successful Ajax Post always returns fail so i just did this
			switch (err.responseText) {
				case "No User":
					console.log(err.responseText)
					$("#username").addClass(".is-invalid")
					setTimeout( () => {
						$("#username").removeClass(".is-invalid")
					}, 2000)
					break

				case "Incorrect login":
					console.log(err.responseText)
					$("#username").addClass(".is-valid")
					$("#password").addClass(".is-invalid")
					setTimeout(() => {
						$("#username").removeClass(".is-valid")
					}, 2000)
					setTimeout(() => {
						$("#password").removeClass(".is-invalid")
					}, 2000)
					break

				case "Success":
					console.log(err.responseText)
					$("#username").addClass(".is-valid")
					$("#password").addClass(".is-valid")
					setTimeout(() => {
						$("#username").removeClass(".is-valid")
					}, 2000)
					setTimeout(() => {
						$("#password").removeClass(".is-valid")
					}, 2000)
					window.location.href = "../dash"
					break

				default:
					console.log(err.responseText)
					break
			}
		})
	})

	$(".register-submit").on('click', async (e) => {
		e.preventDefault()

		console.log("Regestering user")
		

		var user, email, pass = [false, false, false]

		var formData = {
			"type": "register",
			"username": $("#register-username").val(),
			"email": $("#register-email").val(),
			"password": $("#register-pass1").val(),
			"passCheck": $("#register-pass2").val()
		}
		console.log(formData)
		if (formData["password"] === formData["passCheck"]){
			pass = true
		}
		if (/(.+)@(.+){2,}\.(.+){2,}/.test(formData["email"])){
			email = true
		}
		if (formData['username'].length >= 3){
			user = true
		}

		console.log({user, email, pass})

		if (user && email && pass)  {
			$.ajax({
				url: window.location,
				method: "POST",
				data: JSON.stringify(formData),
				contentType: "application/json charset=utf-8",
				dataType: "json"
			}).fail( (err) => {
				console.log(err)
				console.log(err.responseText)
			})
		}
	})
})