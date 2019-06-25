from app.data import db


class Base(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f"<{self.table_name}, {self.id}>"

from app.data.models._class import Class
from app.data.models.link import (
    Access,
    Roll_Student,
    Class_Student,
)
from app.data.models.station import Station
from app.data.models.roll import Roll
from app.data.models.student import Student
from app.data.models.user import User

models = [
    Class,
    Access,
    Roll_Student,
    Class_Student,
    Station,
    Roll,
    Student,
    User,
]

models = {x.__name__: x for x in models}
