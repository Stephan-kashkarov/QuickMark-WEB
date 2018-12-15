from app import db

class Class(db.Model):
	__tablename__ = "class"

	id =    db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(50))
	roll = db.relationship('Roll_Class', backref='class', lazy='dynamic')

	def __repr__(self):
		return "<Class: {}>".format(self.title)

class Roll(db.Model):
	__tablename__ = "roll"

	class_id =   db.Column(db.Integer, db.ForeignKey('class.id'),  primary_key=True)
	student_id = db.Column(db.Integer, db.ForeignKey('person.id'), primary_key=True)

	def __repr__(self):
		return "<Roll object Student: {} is in Class: {}>".format(self.student_id, self.class_id)


class Person(db.Model):
	__tablename__ = "person"

	id =           db.Column(db.Integer, primary_key=True)
	student_id =   db.Column(db.Integer)
	student_name = db.Column(db.String(50))
	rfid =         db.Column(db.Blob)
	roll =         db.relationship('Roll_Person', backref='person', lazy='dynamic')

	def __repr__(self):
		return "<Student, id: {}, name: {}, dbId: {}>".format(self.student_id, self.student_name, self.id)
