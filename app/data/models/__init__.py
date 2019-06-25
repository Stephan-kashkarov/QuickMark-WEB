from app.data import db
from app.data.models._class import Class
from app.data.models.station import Station
from app.data.models.roll import Roll
from app.data.models.student import Student
from app.data.models.user import User
from app.data.models.link import (
    Access,
    Roll_Student,
    Class_Student,
)

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
