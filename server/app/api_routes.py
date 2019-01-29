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

from server.app import app, db
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

@app.route("/api", methods=["POST"])
def API():
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
