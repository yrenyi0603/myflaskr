import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
# app = Flask(__name__)
from flask_admin import Admin
from logging.config import dictConfig

db = SQLAlchemy()
admin = Admin(name='HRO测试Mock服务', template_mode='bootstrap4')

HOST = '192.168.8.152'
PORT = '3307'
DATABASE = 'flaskr'
USERNAME = 'root'
PASSWORD = '123456'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,
                                                                                        password=PASSWORD, host=HOST,
                                                                                        port=PORT, db=DATABASE)

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},

    'handlers': {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default',

        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            # 'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default',
            'filename': 'logconfig.log',
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 3

        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['file']
    }
})


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
        SQLALCHEMY_DATABASE_URI=DB_URI,
        SQLALCHEMY_TRACK_MODIFICATIONS=True,
        FLASK_ADMIN_SWATCH='cerulean'
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    # try:
    #     # os.makedirs(app.instance_path)
    # except OSError:
    #     pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    db.init_app(app)
    admin.init_app(app=app, )

    from . import smstemplateview
    from . import modelview
    app.register_blueprint(smstemplateview.tp)
    app.register_blueprint(modelview.modv)
    return app
