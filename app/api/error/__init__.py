from flask import Blueprint

error = Blueprint('error', __name__)

from app.api.error import controllers
