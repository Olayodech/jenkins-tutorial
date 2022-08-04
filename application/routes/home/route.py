from flask import render_template
from application.routes.home import bp
from application.models import Product


# @app.route('/')
# @app.route('/index')
@bp.route('/')
@bp.route('/index')
def index():
    user = {'username': 'Charles'}
    items = [
        {   'id': 1,
            'name': 'Dior',
            'price': 5000,
            'discount': 0,
            'description': 'Dior exclesior, branded to suit you',
            'image': "dior.png"
        },
        {
            'id': 2,
            'name': 'LV',
            'price': 13000,
            'discount': 0,
            'description': 'LV deluxe, branded to suit you',
            'image': "lv.png"
        }
    ]
    products = Product.query.all()
    return render_template('/home/index.html', title='Home', user=user, items=items, products = products)