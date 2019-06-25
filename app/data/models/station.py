from app.data import db


class Station(db.Model):
    __tablename__ = "station"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
    linked_roll = db.Column(db.Integer, db.ForeignKey('roll.id'))
    linked_roll_rel = db.relationship("Roll", back_populates="linked_rfid")
    scan = db.Column(db.Integer)
    active = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<Station {}>'.format(self.name)

    def set_password(self, password):
        """Runs the passwords through a hash and appends."""
        self.password_hash = generate_password_hash(str(password))

    def check_password(self, password):
        """Checks a password against the hash."""
        return check_password_hash(self.password_hash, password)

    def get_scan(self):
        return self.scan if not self.active else None
