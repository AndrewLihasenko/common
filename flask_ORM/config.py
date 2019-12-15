import os


PG_USER = "flask_orm"
PG_PASSWORD = "123"
PG_HOST = "localhost"
PG_PORT = 5432
DB_NAME = "flask_orm"
SQLALCHEMY_DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False


class Config:
    SECRET_KEY = "key"
    DEBUG = True


class TestConfig(Config):
    SECRET_KEY = "test_key"
    DEBUG = True


class ProdConfig(Config):
    SECRET_KEY = "prod_key"
    DEBUG = False


def run_config():
    env = os.environ.get("ENV")
    config = {"TEST": TestConfig, "PROD": ProdConfig}
    return config.get(env, Config)
