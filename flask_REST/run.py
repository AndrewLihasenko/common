from flask import Flask, current_app
from config import run_config
from rooms import rooms_bp
from staff import staff_bp
from tenants import tenants_bp

app = Flask(__name__)

app.config.from_object(run_config())

app.register_blueprint(rooms_bp)
app.register_blueprint(staff_bp)
app.register_blueprint(tenants_bp)


@app.route("/")
def hotel():
    return current_app.config["SECRET_KEY"]


if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"])
