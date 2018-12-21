$(function(){
	$(".login-submit").on('click', async(e) => {
		e.preventDefault()
		formData = {
			'username': $("#username").val(),
			'passowrd': $("#password").val(),
			"remember": $("#remember").val()
		}
		$.ajax({
			url: window.location,
			method: "POST",
			data: JSON.stringify(formData),
			contentType: "application/json; charset=utf-8",
			dataType: "json"
		}).fail((err) => { // Successful Ajax Post always returns fail so i just did this
			switch (err.responseText) {
				case "No User":
					console.log(err.responseText)
					$("#username").addClass(".is-invalid")
					setTimeout( () => {
						$("#username").removeClass(".is-invalid")
					}, 2000)
					break;

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
					break;

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
					window.location.href = "../dash";
					break;

				default:
					console.log(err.responseText)
					break;
			}
		})
	})
})