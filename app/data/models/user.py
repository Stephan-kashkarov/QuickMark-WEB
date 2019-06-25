from app import login
from app.data import db
from flask_login import UserMixin


@login.user_loader
def load_user(id):
    """User loader for flask login."""
    return User.query.get(int(id))


class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), nullable=True)
    password_hash = db.Column(db.String(128))
    logins = db.Column(db.Integer, default=0)
    classes = db.relationship("Access", backref="user", lazy="dynamic")

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        """Runs the passwords through a hash and appends."""
        self.password_hash = generate_password_hash(str(password))

    def check_password(self, password):
        """Checks a password against the hash."""
        return check_password_hash(self.password_hash, password)
