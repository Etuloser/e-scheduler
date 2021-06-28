import logging
import os
import time

from flask import Flask
from flask_apscheduler import APScheduler
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SCHEDULER_API_ENABLED = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


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
        scheduler.start()
    from app.task import events

    api = Api(app)
    from app.auth.views import UserApi, UserListApi
    api.add_resource(UserListApi, '/user')
    api.add_resource(UserApi, '/user/<user_id>')

    return app
