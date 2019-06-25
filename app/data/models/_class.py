from app.data import db


class Class(db.Model):
    __tablename__ = "class"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    desc = db.Column(db.String(200))
    users = db.relationship(
        "Access",
        backref="class",
        lazy="dynamic"
    )
    students = db.relationship(
        "Class_Student",
        backref="class",
        lazy="dynamic"
    )

    def __repr__(self):
        return "<Class: {}>".format(self.title)
