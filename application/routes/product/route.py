from flask import render_template, redirect, url_for, flash
# from application.routes.product import bp
# from application.forms.forms import ProductForm
# from application.models import Product
# from application import db

from routes.product import bp
from forms.forms import ProductForm
from models import Product
from app import db


@bp.route('/product_details/<int:id>', methods=['GET'])
def product_details(id):
    # fetch images from database with id 
    # create a table like structure
    # display images
    # description
    # product description
    # full details
    # add to cart 
    # prize
    product = Product.query.filter_by(id=id).first()
    if product is None:
        flash('Sorry, try another product!!!')
        return redirect(url_for('home.index'))   
    return render_template('/product/product_details.html', title='product details', product=product)

@bp.route('/new_product', methods=['GET', 'POST'])
def new_product():
    form = ProductForm()
    if form.validate_on_submit():
        product = Product(name=form.name.data, description=form.description.data, price=form.price.description, brand=form.brand.data,
                            category=form.category.data, image=form.image.data)
        db.session.add(product)
        db.session.commit()
        flash('Product successfully created!!!')
        return redirect(url_for('home.index'))
    return render_template('/product/new_product.html', title="Create Product", form=form)