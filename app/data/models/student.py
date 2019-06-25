from app.data import db
from app.data.models import Base


class Student(Base):
    __tablename__ = "student"

    student_id = db.Column(db.Integer)
    student_name = db.Column(db.String(50))
    rfid = db.Column(db.Integer)
    roll = db.relationship("Roll_Student", backref="student", lazy="dynamic")

    def __repr__(self):
        return "<Student, id: {}, name: {}, dbId: {}>".format(
            self.student_id,
            self.student_name,
            self.id,
        )
