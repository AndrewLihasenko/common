import os


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
