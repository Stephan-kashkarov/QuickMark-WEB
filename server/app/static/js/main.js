$(function(){
	$(".nav-login").on('click', function(e){
		e.preventDefault()
		window.location.href = "http://127.0.0.1:5000/auth/login"
	})
	$(".nav-register").on('click', function(e){
		e.preventDefault()
		window.location.href = "http://127.0.0.1:5000/auth/register"
	})
})