from app.data import db


class Access(db.Model):
    __tablename__ = "access"

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        primary_key=True
    )
    class_id = db.Column(
        db.Integer,
        db.ForeignKey("class.id"),
        primary_key=True
    )


class Roll_Student(db.Model):
    __tablename__ = "roll_student"
    extend_existing = True
    roll_id = db.Column(
        db.Integer,
        db.ForeignKey("roll.id"),
        primary_key=True
    )
    student_id = db.Column(
        db.Integer,
        db.ForeignKey("student.id"),
        primary_key=True
    )
    present = db.Column(
        db.Boolean,
        default=False
    )
    marked_at = db.Column(
        db.DateTime,
        default=None
    )


class Class_Student(db.Model):
    __tablename__ = "class_student"

    roll_id = db.Column(
        db.Integer,
        db.ForeignKey("class.id"),
        primary_key=True
    )
    student_id = db.Column(
        db.Integer,
        db.ForeignKey("student.id"),
        primary_key=True
    )
