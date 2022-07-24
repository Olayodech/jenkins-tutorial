from application import app
from flask import render_template

@app.route('/')
@app.route('/index')
def getHome():
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
    return render_template('index.html', title='Home', user=user, items=items)