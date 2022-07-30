from flask import render_template
from application.routes.home import bp


# @app.route('/')
# @app.route('/index')
@bp.route('/')
@bp.route('/index')
def index():
    user = {'username': 'Charles'}
    items = [
        {
            'name': 'Dior',
            'price': 5000,
            'discount': 0,
            'description': 'Dior exclesior, branded to suit you',
            'image': "dior.png"
        },
        {
            'name': 'LV',
            'price': 13000,
            'discount': 0,
            'description': 'LV deluxe, branded to suit you',
            'image': "lv.png"
        }
    ]
    return render_template('/home/index.html', title='Home', user=user, items=items)