from flask_migrate import Migrate
from flask_login import LoginManger
from flask_cors import CORS
from flask import Flask

from app.config import configure_app
from app.data import db

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

from app.api import api
app.register_blueprint(api, prefix=f'/api')


app.url_map.strict_slashes = False