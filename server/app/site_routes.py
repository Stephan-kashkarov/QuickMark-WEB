from server.app import app, db
from flask import redirect, url_for, flash, render_template, request
from server.app.models import Class, Roll, Student, Person , Access

from flask_login import current_user, login_user, login_required, logout_user

@app.route("/")
def index():
	return render_template("body.html")

@app.route("/auth")
def auth():
	return render_template("auth.html")

@app.route("/dash")
@login_required
def dash():
	user = current_user
	classes = [Class.query.get(x) for x in Access.query.filter_by(person_id=user.id)]
	rolls = [Roll.query.filter_by(class_id=x.id) for x in classes]
	if classes:
		print(user, classes)
	return render_template("dash.html", user=user, classes=classes, rolls=rolls)


@app.route("/class")
@login_required
def classes():
	return "WIP"

@app.route("/class/<c_id>")
@login_required
def class_id(c_id):
	return "WIP"

@app.route("/class/make")
@login_required
def class_make():
	return render_template('class_make.html')

