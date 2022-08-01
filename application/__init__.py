from flask import Flask
from flask_material import Material
from config import Config, DevConfig, ProdConfig
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
material =Material()
migrate = Migrate()
login = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    if app.config['ENV'] == 'production':
        app.config.from_object(ProdConfig)
    else:
        app.config.from_object(DevConfig)

    db.init_app(app)
    material.init_app(app)
    migrate.init_app(app, db)
# app.config.from_object(Config)

    login.init_app(app)

    from application.routes.home import bp as home_bp
    from application.routes.users import bp as users_bp
    app.register_blueprint(home_bp)
    app.register_blueprint(users_bp, url_prefix='/user')

    return app

login.login_view = 'login'

from application import models