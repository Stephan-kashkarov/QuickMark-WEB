from app.api.roll import roll as roll_bp
from app.api.user import user as user_bp
from app.api.error import error as error_bp
from app.api.station import station as station_bp

from flask import Blueprint

controllers = [
    ('/class', roll_bp),
    ('/station', station_bp),
    ('/user', user_bp),
    ('/error', error_bp),
]