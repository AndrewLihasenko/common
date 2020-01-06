from datetime import timedelta
from flask import Flask

from config import run_config
from create_db import create_db
from db import db, migrate
from rooms import rooms_bp
from staff import staff_bp
from tenants import tenants_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(run_config())

    db.init_app(app)
    migrate.init_app(app, db)
    app.permanent_session_lifetime = timedelta(minutes=20)

    app.register_blueprint(create_db)
    app.register_blueprint(rooms_bp)
    app.register_blueprint(staff_bp)
    app.register_blueprint(tenants_bp)

    return app
