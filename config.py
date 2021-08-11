import logging
import os
import time
from urllib import parse

from dotenv import load_dotenv
from flask import Flask
from flask_apscheduler import APScheduler
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SCHEDULER_API_ENABLED = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True

    user = os.environ.get('DB_USER')
    pwd = parse.quote_plus(os.environ.get('DB_PWD'))
    host = os.environ.get('DB_HOST')
    db = os.environ.get('DB_NAME')

    db_url = f'mysql+pymysql://{user}:{pwd}@{host}:3306/{db}?charset=utf8'

    SQLALCHEMY_DATABASE_URI = db_url or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True

    user = os.environ.get('DB_USER')
    pwd = parse.quote_plus(os.environ.get('DB_PWD'))
    host = os.environ.get('DB_HOST')
    db = os.environ.get('DB_NAME')

    db_url = f'mysql+pymysql://{user}:{pwd}@{host}:3306/{db}?charset=utf8'

    SQLALCHEMY_DATABASE_URI = db_url or 'sqlite:///' + \
        os.path.join(basedir, 'data-test.sqlite')
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    user = os.environ.get('DB_USER')
    pwd = parse.quote_plus(os.environ.get('DB_PWD'))
    host = os.environ.get('DB_HOST')
    db = os.environ.get('DB_NAME')

    db_url = f'mysql+pymysql://{user}:{pwd}@{host}:3306/{db}?charset=utf8'

    SQLALCHEMY_DATABASE_URI = db_url or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    KAFKA_URI = os.environ.get('KAFKA_URI')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}

db = SQLAlchemy()
scheduler = APScheduler()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)

    scheduler.init_app(app)
    logging.getLogger("apscheduler").setLevel(logging.INFO)
    with app.app_context():
        from app.task import tasks
        # disable debug mode while scheduler running
        # scheduler.start()
    from app.task import events

    api = Api(app)
    from app.auth.views import UserApi, UserListApi
    api.add_resource(UserListApi, '/user')
    api.add_resource(UserApi, '/user/<user_id>')

    from app.status.views import status as status_blueprint
    app.register_blueprint(status_blueprint, url_prefix='/status')

    return app
