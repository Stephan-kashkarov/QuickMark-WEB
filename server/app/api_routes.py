import re
import json
import pprint

from flask import (
    flash,
    jsonify,
    redirect,
    render_template,
    request,
    url_for
)
from flask_login import (
    login_required,
    login_user,
    logout_user,
    current_user
)

from server.app import (
    app,
    db
)

from server.app.models import (
    Class,
    Class_Student,
    Person,
    RFIDStation,
    Roll,
    Roll_Student,
    Student
)

from datetime import datetime

def authStation(s_id, password):
    station = RFIDStation.query.get_or_404(int(s_id))
    if station and station.check_password(password):
        return station
    return False

# Auth stuff
@app.route("/api/auth/login", methods=["POST"])
def login():
    if request.is_json:
        data = request.get_json()
        user = Person.query.filter_by(username=data['username']).first()
        if not user:
            user = Person.query.filter_by(email=data['username']).first_or_404()
        if user.check_password(data['password']):
            login_user(user, remember=data['remember'])
            return 'Login successful', 201
        return "Login unsuccsessful - incorrect password"
    return "Login unsuccsessful - No user found"

@app.route("/api/auth/register", methods=["POST"])
def register():
    if request.is_json:
        data = request.get_json()
        if not Person.query.filter_by(username=data['username']).first():
            user = Person()
            user.username = data['username']
            user.email = data['email']
            user.set_password(data['password'])
            db.session.add(user)
            db.session.commit()
            return "Registration Succsesful - try logging in", 201
        return "Registration unsuccsesful - User already exists"
    return "Registration unsuccsesful - data 404"

@login_required
@app.route("/api/auth/logout", methods=["POST"])
def logout():
    logout_user()
    return "Logout Succsesful"


# RFID stuff
@app.route("/api/rfid", methods=["POST"])
def rfid():
    data = request.get_json()
    if data:
        auth = data['auth']
        station = authStation(auth['id'], auth['key'])
        if station:
            data = data['payload']
            student = Student.query.filter_by(uid=data['uid']).first_or_404()
            marking_instance = Roll_Student.query.filter_by(student_id=student.id, roll_id=station.linked_roll)
            marking_instance.present = True
            marking_instance.marked_at = datetime.now()

            return "Operation succsessful"
        return "Invalid auth details"
    return "No Json"
