from server.app import db, login
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

@login.user_loader
def load_user(id):
	"""User loader for flask login."""
	return Person.query.get(int(id))

# INTERMIDEARY TABLES
class Access(db.Model):
	__tablename__ = "access"

	person_id = db.Column(db.Integer, db.ForeignKey("person.id"), primary_key=True)
	class_id =  db.Column(db.Integer, db.ForeignKey("class.id"), primary_key=True)

class Roll_Student(db.Model):
	__tablename__ = "roll_student"
	extend_existing = True
	roll_id =    db.Column(db.Integer, db.ForeignKey("roll.id"), primary_key=True)
	student_id = db.Column(db.Integer, db.ForeignKey("student.id"), primary_key=True)
	present =    db.Column(db.Boolean, default=False)
	marked_at =  db.Column(db.DateTime, default=None)

class Class_Student(db.Model):
	__tablename__ = "class_student"

	roll_id = db.Column(db.Integer, db.ForeignKey("class.id"), primary_key=True)
	student_id = db.Column(db.Integer, db.ForeignKey("student.id"), primary_key=True)


# DATA TABLES
class Class(db.Model):
	__tablename__ = "class"

	id =           db.Column(db.Integer, primary_key=True)
	title =        db.Column(db.String(50))
	desc =         db.Column(db.String(200))
	users =        db.relationship("Access", backref="class", lazy="dynamic")
	students =     db.relationship("Class_Student", backref="class", lazy="dynamic")

	def __repr__(self):
		return "<Class: {}>".format(self.title)


class Student(db.Model):
	__tablename__ = "student"

	id =           db.Column(db.Integer, primary_key=True)
	student_id =   db.Column(db.Integer)
	student_name = db.Column(db.String(50))
	rfid =         db.Column(db.Integer)
	roll =         db.relationship("Roll_Student", backref="student", lazy="dynamic")

	def __repr__(self):
		return "<Student, id: {}, name: {}, dbId: {}>".format(self.student_id, self.student_name, self.id)


class Roll(db.Model):
	__tablename__ = "roll"

	id =       db.Column(db.Integer, primary_key=True)
	time =     db.Column(db.DateTime, default=datetime.now())
	class_id = db.Column(db.Integer)
	roll =     db.relationship("Roll_Student", backref="roll", lazy="dynamic")
	linked_rfid = db.relationship("RFIDStation", back_populates="linked_roll_rel")

	def __repr__(self):
		return "<Roll object Student: {} is in Class: {}>".format(self.student_id, self.class_id)

# USER TABLES
class Person(db.Model, UserMixin):
	__tablename__ = "person"

	id =            db.Column(db.Integer, primary_key=True)
	username =      db.Column(db.String(64), index=True, unique=True)
	email =         db.Column(db.String(120), nullable=True)
	password_hash = db.Column(db.String(128))
	logins =        db.Column(db.Integer, default=0)
	classes =       db.relationship("Access", backref="person", lazy="dynamic")

	def __repr__(self):
		return '<User {}>'.format(self.username)

	def set_password(self, password):
		"""Runs the passwords through a hash and appends."""
		self.password_hash = generate_password_hash(str(password))

	def check_password(self, password):
		"""Checks a password against the hash."""
		return check_password_hash(self.password_hash, password)

class RFIDStation(db.Model):
	__tablename__ = "rfid_station"
	id =              db.Column(db.Integer, primary_key=True)
	name =            db.Column(db.String(64))
	password_hash =   db.Column(db.String(128))
	linked_roll =     db.Column(db.Integer, db.ForeignKey('roll.id'))
	linked_roll_rel = db.relationship("Roll", back_populates="linked_rfid")
	scan =            db.Column(db.Integer)
	scanning =        db.Column(db.Boolean, default=False)

	def __repr__(self):
		return '<Station {}>'.format(self.name)

	def set_password(self, password):
		"""Runs the passwords through a hash and appends."""
		self.password_hash = generate_password_hash(str(password))

	def check_password(self, password):
		"""Checks a password against the hash."""
		return check_password_hash(self.password_hash, password)

	def get__scan(self):
		return self.scan if not self.scanning else None
