from flask import Blueprint

station = Blueprint('station', __name__)

from app.api.station import controllers