from flask import Flask
from flask_material import Material
from application.routes.home import bp as home_bp
from config import Config, DevConfig, ProdConfig
from flaskext.mysql import MySQL

app = Flask(__name__)

if app.config['ENV'] == 'production':
    app.config.from_object(ProdConfig)
else:
    app.config.from_object(DevConfig)

app.config.from_object(Config)
Material(app)

mysql = MySQL(app)
mysql.init_app(app)

app.register_blueprint(home_bp)
from application import routes