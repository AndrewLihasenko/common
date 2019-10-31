from flask import Flask, render_template
from utils import get_data

app = Flask(__name__)


@app.route('/')
def get_home_page():
    return render_template("home.html", data=get_data())

@app.route('/alarm_clock')
def get_alarm_clock_page():
    return render_template("alarm_clock.html", data=get_data())

@app.route('/headphones')
def get_headphones():
    return render_template("headphones.html", data=get_data())

@app.route('/iPod')
def get_iPod():
    return render_template("iPod.html", data=get_data())

@app.route('/calculator')
def get_calculator():
    return render_template("calculator.html", data=get_data())

@app.route('/coffeemaker')
def get_coffeemaker():
    return render_template("coffeemaker.html", data=get_data())

@app.route('/battery_charger')
def get_battery_charger():
    return render_template("battery_charger.html", data=get_data())

@app.route('/author')
def get_author_page():
    return render_template("author.html")


if __name__ == "__main__":
    app.run(debug=True)
