from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from application import db, login


class Product(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(125), index=True, unique=True)
    description = db.Column(db.String(250))
    price = db.Column(db.String(6))
    discount = db.Column(db.String(6))
    brand = db.Column(db.String(10))
    category = db.Column(db.String(10))
    image = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Product {}>'.format(self.name)


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index = True, unique=True)
    first_name = db.Column(db.String(55))
    last_name = db.Column(db.String(55))
    address = db.Column(db.String(55))
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(120), index=True, unique=True)

    def setCustomerPassword(self, password):
        self.password_hash = generate_password_hash(password)

    def validatePassword(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<customer {}>'.format(self.name)
    
@login.user_loader
def loadCustomer(id):
    return Customer.query.get(int(id))