from flask import render_template, redirect, url_for, flash
from application.routes.users import bp
from application.forms.forms import RegisterationForm
from application.models import Customer
from application import db
from flask_login import current_user, login_user, logout_user
from application.forms.forms import LoginForm

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        customer = Customer.query.filter_by(username=form.username.data).first()
        if customer is None or not customer.validatePassword(form.password.data):
            flash('Incorrect credentials, please try again')
            return redirect(url_for('users.login'))
        # login_user(customer, remember=form.rememberMe.data)
        return redirect(url_for('home.index'))
    return render_template('/users/login.html', title='Login', form=form)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterationForm()
    if form.validate_on_submit():
        customer = Customer(username=form.username.data, first_name=form.firstName.data, last_name= form.lastName.data,
                            address=form.address.data, email=form.email.data)
        customer.setCustomerPassword(form.password.data)
        db.session.add(customer)
        db.session.commit()
        flash('Registeration successful, please login with your username')
        return redirect(url_for('users.login'))
    return render_template('/users/registration.html', title='Registration', form=form)

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home.index'))

@bp.route('/profile', methods=['GET', 'POST'])
def profile():

    return render_template('/users/index.html', title='Registration', form=form)
