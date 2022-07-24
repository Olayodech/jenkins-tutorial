from flask import Flask
from flask_material import Material
from application.routes.home import bp as home_bp

app = Flask(__name__)
Material(app)

app.register_blueprint(home_bp)
from application import routes