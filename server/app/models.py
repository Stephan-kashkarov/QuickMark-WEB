from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login.user_loader
def load_user(id):
	"""User loader for flask login."""
	return Person.query.get(int(id))

class Class(db.Model):
	__tablename__ = "class"

	id =    db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(50))
	roll =  db.relationship('Roll_Class', backref='class', lazy='dynamic')

	def __repr__(self):
		return "<Class: {}>".format(self.title)

class Roll(db.Model):
	__tablename__ = "roll"

	class_id =   db.Column(db.Integer, db.ForeignKey('class.id'),  primary_key=True)
	student_id = db.Column(db.Integer, db.ForeignKey('student.id'), primary_key=True)

	def __repr__(self):
		return "<Roll object Student: {} is in Class: {}>".format(self.student_id, self.class_id)


class Student(db.Model):
	__tablename__ = "student"

	id =           db.Column(db.Integer, primary_key=True)
	student_id =   db.Column(db.Integer)
	student_name = db.Column(db.String(50))
	rfid =         db.Column(db.BLOB)
	roll =         db.relationship('Roll_student', backref='student', lazy='dynamic')

	def __repr__(self):
		return "<Student, id: {}, name: {}, dbId: {}>".format(self.student_id, self.student_name, self.id)


class Person(db.Model, UserMixin):
	__tablename__ = "person"

	id =            db.Column(db.Integer, primary_key=True)
	username =      db.Column(db.String(64), index=True, unique=True)
	password_hash = db.Column(db.String(128))

	def __repr__(self):
		return '<User {}>'.format(self.username)

	def set_password(self, password):
		"""Runs the passwords through a hash and appends."""
		self.password_hash = generate_password_hash(str(password))

	def check_password(self, password):
		"""Checks a password against the hash."""
		return check_password_hash(self.password_hash, password)