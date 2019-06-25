from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_login import LoginManager

from config import configure_app

from app.data import db
from app.data.models import models
from app.api import controllers

app = Flask(__name__)

configure_app(app, 'dev')

cors = CORS(app, resources={
    r'/api/*': {
        'origins': app.config.ORIGINS
    }
})

db.init_app(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'api.user.login'

for prefix, bp in controllers:
    app.register_blueprint(bp, prefix=f"/api{prefix}")


app.url_map.strict_slashes = False
