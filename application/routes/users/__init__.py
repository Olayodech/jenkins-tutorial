from flask import Blueprint
bp = Blueprint('users', __name__)

# from application.routes.users import route
from routes.users import route