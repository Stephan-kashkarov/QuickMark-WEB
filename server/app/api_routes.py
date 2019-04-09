import re
import json
import pprint

from flask import (
    jsonify,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import (
    login_required,
    login_user,
    logout_user,
    current_user,
)

from server.app import (
    app,
    db,
)

from server.app.models import (
    Class,
    Class_Student,
    Person,
    RFIDStation,
    Roll,
    Roll_Student,
    Student,
    Access,
)

import server.app.models as models


model_dict = {
    str(y).lower() if y else None: eval(y) if y else None for y in set(
        [
            x
            if not x.startswith("_")
            and x[0].isupper()
            and x not in ['UserMixin']
            else None
            for x in dir(models)
        ]
    )
}

from datetime import datetime

def authStation(s_id, password):
    station = RFIDStation.query.get_or_404(int(s_id))
    if station and station.check_password(password):
        return station
    return False

################################################################
####################### Auth stuff #############################
################################################################

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

@app.route("/api/auth/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return "Logout Succsesful"


################################################################
###################### Create stuff ############################
################################################################

@app.route("/api/class/make", methods=["POST"])
@login_required
def class_gen():
    if request.is_json:
        data = request.get_json()
        try:
            c = Class()
            c.title = data['title']
            c.desc = data['desc']
            db.session.add(c)
            a = Access()
            a.class_id = c.id
            a.person_id = current_user.id
            db.session.add(a)
            for student_id in data['students']:
                link = Class_Student()
                link.student_id = student_id
                link.roll_id = c.id
            db.session.commit()
            return "Successfully created class"
        except KeyError:
            return "Invalid JSON format"
    return "Couldn't create class - data 404"

@app.route("/api/student/make", methods=["POST"])
@login_required
def student_gen():
    if request.is_json:
        data = request.get_json()
        try:
            s = Student()
            s.student_id = data['id']
            s.student_name = data['name']
            s.rfid = data['rfid']
            db.session.add(s)
            db.session.commit()
            return "Student created successfully"
        except KeyError:
            return "Invalid JSON format"
    return "Couldn't create student - data 404"


################################################################
######################## DB stuff ##############################
################################################################

@app.route("/api/db/query/<class_name>", methods=['POST'])
def student_db(class_name):
    if request.is_json:
        data = request.get_json()
        print(data)
        try:
            query = [
                x.as_dict() for x in model_dict[
                    class_name.lower()
                ].query.filter(
                    eval(data['key']).contains(data['val'])
                ).all()
            ]
            print(f"The result of query: {query}")
            return jsonify(
                query
            ), 200
        except KeyError:
            return "Invalid JSON format", 400
    return "Couldn't query - data 404", 404



################################################################
####################### RFID stuff #############################
################################################################

@app.route("/api/rfid", methods=["POST"])
def rfid():
    data = request.get_json()
    if data:
        auth = data['auth']
        station = authStation(auth['id'], auth['key'])
        if station:
            data = data['payload']
            student = Student.query.filter_by(uid=data['uid']).first()
            if station.scanning:
                station.scanning = False
                station.scan = data['uid']
            elif station.linked_roll():
                marking_instance = Roll_Student.query.filter_by(student_id=student.id, roll_id=station.linked_roll)
                marking_instance.present = True
                marking_instance.marked_at = datetime.now()
            return "Operation succsessful"
        return "Invalid auth details"
    return "No Json"


@app.route("/api/get_rfid", methods=["POST"])
@login_required
def rfid_get():
    if request.is_json:
        data = request.get_json()
        print(data)
        station = RFIDStation.query.get_or_404(data['rfid_id'])
        if station.scanning and not station.scan:
            station.scanning = True
            return "Scanning", 404
        elif station.scan:
            station.scanning = False
            return jsonify(station.get_scan()), 201
        return jsonify("Starting scan"), 200

    return "input not json"
