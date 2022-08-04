from flask import Blueprint

bp = Blueprint('product', __name__)

from application.routes.product import route