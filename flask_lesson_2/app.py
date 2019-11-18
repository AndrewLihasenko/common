from flask import Flask, render_template
from products.main import product
from supermarkets.main import supermarket

app = Flask(__name__)

app.register_blueprint(product)
app.register_blueprint(supermarket)
app.config['SECRET_KEY'] = '123'


@app.route('/')
@app.route('/home')
def get_home_page():
    return render_template("home.html")


@app.errorhandler(404)
def page_not_found(error):
    render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
