from server.app import app, db
from flask import redirect, url_for, flash, render_template, request
from server.app.models import Class, Roll, Student, Person 

from flask_login import current_user, login_user, login_required, logout_user

@app.route("/")
def index():
	return render_template("body.html")

@login_required
@app.route("/dash")
def dash():
	return render_template("dash.html")

