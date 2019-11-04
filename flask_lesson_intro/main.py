from flask import Flask, render_template
from utils import get_data
import errors

app = Flask(__name__)


@app.route('/')
def get_home_page():
    return render_template("home.html", data=get_data())

@app.route('/<item>')
def get_items(item):
    data = get_data()
    if item in [dct['title'] for dct in data]:
        for dct in data:
            if item == dct['title']:
                text = dct["text"]
                return render_template('item.html', item=item, text=text)
    else:
        return errors.page_not_found(404)

@app.route('/author')
def get_author_page():
    return render_template("author.html")


if __name__ == "__main__":
    app.run(debug=True)
