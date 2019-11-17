import os
import uuid

from flask import Blueprint, render_template, request, url_for, session
from werkzeug.utils import redirect

from forms import AddProductForm
from utils import set_data, get_data


product = Blueprint('products', __name__,
                    template_folder='template',
                    static_folder='static',
                    static_url_path='/static/product')


LIST_PRODUCT = 'products.json'
UPLOAD_FOLDER = './products/static'


@product.route('/add_product', methods=['GET', 'POST'])
def add_product():
    form = AddProductForm()
    return render_template('add_product.html', form=form)


@product.route('/product', methods=['POST'])
def save_product():
    file = request.files['image']

    prod = {
        "id": str(uuid.uuid1()),
        "name": request.form.get('name'),
        "description": request.form.get('description'),
        "img_name": file.filename,
        "price": request.form.get('price')
    }
    if get_data(LIST_PRODUCT):
        data = get_data(LIST_PRODUCT)
        data.append(prod)
        set_data(data, LIST_PRODUCT)
    else:
        set_data([prod], LIST_PRODUCT)

    if file:
        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)
    return redirect(url_for('products.get_products'))


@product.route('/all_products', methods=['GET'])
def get_products():
    data = get_data(LIST_PRODUCT)
    return render_template('all_products.html', data=data)


@product.route('/all_products', methods=['POST'])
def get_products_by_filter():
    return redirect(url_for('products.get_products?price=<price>',
                            price=request.form.get('price')))


@product.route('/product/<prod_id>', methods=['GET'])
def get_product_id(prod_id):
    data = get_data(LIST_PRODUCT)
    for dct in data:
        if prod_id == dct['id']:
            session[dct['id']] = True
            return render_template('product.html',
                                   description=dct['description'],
                                   prod_id=dct['id'],
                                   img_name=dct['img_name'],
                                   name=dct['name'],
                                   price=dct['price'])
    return render_template("404.html")
