from server.app import app, db
from server.app.models import Person, Class, Roll, Student, RFIDStation


@app.shell_context_processor
def context():
	"""Context for Flask shell .
	This allows for quick tesing of my database
	in the flask shell rather then having to import
	every model in the database
	"""
	return {
		'db': db,
		'Person': Person,
		'Class': Class,
		'Student': Student,
		'Roll': Roll
	}
