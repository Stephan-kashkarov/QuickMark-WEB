from server.app import app, db
from flask import redirect, url_for, flash, render_template, request
from server.app.models import Class, Roll, Student, Person 

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
	return render_template("dash.html")

