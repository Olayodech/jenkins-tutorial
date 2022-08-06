from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, FileField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from models import Customer

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    rememberMe = BooleanField('Remember Me')
    submit = SubmitField('Sign In')



class RegisterationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    firstName = StringField('First Name', validators=[DataRequired()])
    lastName = StringField('Last Name', validators=[DataRequired()])
    address=StringField('Address', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmPassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validateUserName(self, username):
        customer = Customer.query.filter_by(username=username.data).first()
        if customer is not None:
            raise ValueError('Username is either in use or not valid')

    def validate_email(self, email):
        customer = Customer.query.filter_by(email=email.data).first()
        if customer is not None:
            raise ValidationError('Email or username is not valid.')



class ProductForm(FlaskForm):
    name =StringField('Product Name', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    discount = StringField('Discount', validators=[DataRequired()])
    brand = StringField('Brand', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    image = FileField(validators=[DataRequired()])
    submit = SubmitField('Create Product')
