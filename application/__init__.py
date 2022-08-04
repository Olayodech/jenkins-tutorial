from flask import Flask
from flask_material import Material
# from config import Config, DevConfig, ProdConfig
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
material =Material()
migrate = Migrate()
login = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    # if app.config['ENV'] == 'production':
    #     app.config.from_object(ProdConfig)
    # else:
    #     app.config.from_object(DevConfig)
    app.config.from_object(Config)
    print("Database in use "+ app.config['SQLALCHEMY_DATABASE_URI'])
    db.init_app(app)
    material.init_app(app)
    migrate.init_app(app, db)

    login.init_app(app)

    from application.routes.home import bp as home_bp
    from application.routes.users import bp as users_bps
    from application.routes.product import bp as product_bps

    app.register_blueprint(home_bp)
    app.register_blueprint(users_bps, url_prefix='/user')
    app.register_blueprint(product_bps, url_prex='/product')

    # if app.config['LOG_TO_STDOUT']:
    #         stream_handler = logging.StreamHandler()
    #         stream_handler.setLevel(logging.INFO)
    #         app.logger.addHandler(stream_handler)
    # else:
    #     if not os.path.exists('logs'):
    #         os.mkdir('logs')
    #     file_handler = RotatingFileHandler('logs/jenkins-tut-project.log',
    #                                         maxBytes=10240, backupCount=10)
    #     file_handler.setFormatter(logging.Formatter(
    #         '%(asctime)s %(levelname)s: %(message)s '
    #         '[in %(pathname)s:%(lineno)d]'))
    #     file_handler.setLevel(logging.INFO)
    #     app.logger.addHandler(file_handler)

    #     app.logger.setLevel(logging.INFO)
    #     app.logger.info('Mepot up')

    return app

login.login_view = 'login'

from application import models