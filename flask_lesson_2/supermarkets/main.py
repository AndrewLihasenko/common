import os
import uuid

from flask import Blueprint, render_template, request, url_for, session
from werkzeug.utils import redirect

from forms import AddSupermarketForm
from utils import get_data, set_data

supermarket = Blueprint('supermarkets', __name__,
                        template_folder='template',
                        static_folder='static',
                        static_url_path='/static/supermarket')


LIST_SUPERMARKET = 'supermarkets.json'
UPLOAD_FOLDER = './supermarkets/static'


@supermarket.route('/add_supermarket', methods=['GET', 'POST'])
def add_supermarket():
    form = AddSupermarketForm()
    return render_template('add_supermarket.html', form=form)


@supermarket.route('/supermarket', methods=['POST'])
def save_supermarket():
    file = request.files['image']

    supermkt = {
        "id": str(uuid.uuid1()),
        "name": request.form.get('name'),
        "location": request.form.get('location'),
        "img_name": file.filename
    }
    if get_data(LIST_SUPERMARKET):
        data = get_data(LIST_SUPERMARKET)
        data.append(supermkt)
        set_data(data, LIST_SUPERMARKET)
    else:
        set_data([supermkt], LIST_SUPERMARKET)

    if file:
        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)
    return redirect(url_for('supermarkets.get_supermarkets'))


@supermarket.route('/all_supermarkets', methods=['GET'])
def get_supermarkets():
    data = get_data(LIST_SUPERMARKET)
    return render_template('all_supermarkets.html', data=data)


@supermarket.route('/all_supermarkets', methods=['POST'])
def get_supermarkets_by_filter():
    return redirect(url_for('supermarkets.get_supermarkets?location=<location>',
                            price=request.form.get('location')))


@supermarket.route('/supermarket/<supermkt_id>', methods=['GET'])
def get_supermarket_id(supermkt_id):
    data = get_data(LIST_SUPERMARKET)
    for dct in data:
        if supermkt_id == dct['id']:
            session[dct['id']] = True
            return render_template('supermarket.html',
                                   supermkt_id=dct['id'],
                                   img_name=dct['img_name'],
                                   name=dct['name'],
                                   location=dct['location'])
    return render_template("404.html")