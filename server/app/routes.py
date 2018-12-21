from app import app, db
from flask import redirect, url_for, flash, render_template, request
from app.models import Class, Roll, Student, Person 

from flask_login import current_user, login_user, login_required, logout_user

@app.route("/")
def index():
	return render_template("main.html")

@login_required
@app.route("/dash")
def dash():
	return "dash!"

# AUTH ROUTES
@app.route("/auth/login", methods=["GET", "POST"])
def login():
	if request.method == "POST":
		# incase there is no json
		try:
			data = request.json
		except:
			data = None
			flash("Server: No data in json")
			return "No json"

		if data:
			username = data["username"]
			password = data["passowrd"]

			user = Person.query.filter_by(username=username).first()
			if user:
				if user.check_password(password):
					login_user(user)
					flash("Login succsessful!")
					user.logins += 1
					db.session.commit()
					return "Success"
				flash("Login unsucsessful!")
				return "Incorrect login"
			return "No User"
	return render_template("auth/login.html")

@app.route("/auth/register", methods=["GET", "POST"])
def register():
	# incase there is no json
	if request.method == "POST":
		try:
			data = request.json()

		except:
			data = None
			flash("Server: No data in json")

		if data:
			username = data['username']
			email = data['email']
			password = data['password']
			if not Person.query.filter_by(username=username):
				p = Person()
				p.username = username
				p.email = email
				p.set_password(password)
				db.session.add(p)
				db.session.commit(p)
				flash("User created, Try logging in!")
				return redirect(url_for("auth/login"))

	return render_template("auth/register.html")

@login_required
@app.route("/auth/logout", methods=["POST", "GET"])
def logout():
	logout_user()
	return "200"


# CLASS ROUTES
@app.route("/<class_id>/mark")
def mark(class_id):
	students = Roll.query.filter_by(class_id=class_id)
	return "Marking {}".format(class_id)

