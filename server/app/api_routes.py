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


def authStation(s_id, password):
    station = RFIDStation.query.get_or_404(int(s_id))
    if station and station.check_password(password):
        return station
    return False

@app.route("/api/get/class", methods=["POST"])
def apiClassGet():
    data = request.get_json()
    auth = data['auth']
    station = authStation(auth['id'], auth['password'])
    if station:
        data = data['payload']
        roll = Class.query.get(data['class_id'])
        rollObj = Roll()
        rollObj.class_id = roll.id
        db.session.add(rollObj)
        students = Class_Student.query.filter_by(id=int(data['Class_id']))
        for index, student in enumerate(students):
            temp = Roll_Student()
            temp.roll_id = rollObj.id
            temp.student_id = student.id
            db.session.add(temp)
            students[index] = Student.query.get(int(student.student_id))
        db.session.commit()
        print(f"Class queryed: {roll}")
        print(f"The roll contains {len(students)} students:")
        for index, student in enumerate(students):
            print(f"    {index}.  {student}")

        print("Packaging...")
        result = {
            'class': {
                'id': roll.id,
                'title': roll.title,
                'roll': {
                    'roll_id': rollObj.id,
                    'students': [],
                },
            },
        }

        for student in students:
            studentObj = {
                'id': student.id,
                'name': student.name,
                'rfid': student.rfid,
                'present': False,
            }
            result['class']['roll']['students'].append(studentObj)

        print("Packaged!")
        pprint.pprint(result)
        return jsonify([len(json.dumps(result).encode('utf-8')), result])


    return "invalid auth"
