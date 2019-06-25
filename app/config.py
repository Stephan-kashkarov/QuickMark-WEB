class Config:
    ORIGINS = ["*"]
    SECRET_KEY = 'KEY!!'


class Development(Config):
    PORT = 5000
    DEBUG = True
    TESTING = False
    ENV = 'dev'
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class Testing(Config):
    PORT = 5000
    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


config = {
    'dev': Development,
    'prod': Production,
    'test': Testing,
}


def configure_app(app, env='prod'):
    app.config.from_object(config[env])
