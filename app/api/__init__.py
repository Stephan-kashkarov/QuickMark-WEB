from app.api.roll import bp as roll_bp
from app.api.user import bp as user_bp
from app.api.error import bp as error_bp
from app.api.station import bp as station_bp

from flask import Blueprint

controllers = [
    ('/class', roll_bp),
    ('/station', station_bp),
    ('/user', user_bp),
    ('/error', error_bp),
]

api = Blueprint('api', __name__)

for prefix, bp in controllers:
    api.register_blueprint(bp, prefix=prefix)