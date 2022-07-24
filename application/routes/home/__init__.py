from flask import Blueprint

bp = Blueprint('home', __name__)

from application.routes.home import route