from app import app
from flask import redirect, flash, render_template
from app.models import Class, Roll, Student, Person 

@app.route("/")
def index():
	return "Hello!"

@app.route("/home")
def home():
	return "Home!"

# AUTH ROUTES
@app.route("/auth/login")
def login():
	return "login"

@app.route("/<class_id>/mark")
def mark(class_id):
	students = Roll.query.filter_by(class_id=class_id)
	return "Marking {}".format(class_id)

