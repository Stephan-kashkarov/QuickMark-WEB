from flask import Blueprint

user = Blueprint('user', __name__)

from app.api.user import controllers