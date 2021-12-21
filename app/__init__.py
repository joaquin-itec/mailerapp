import os

from flask import Flask
from flask.helpers import safe_join #importacion safe_join para static


def create_app():
    app = Flask(__name__)
    static = safe_join(os.path.dirname(__file__), 'static')  #declaracion de carpeta static

    app.config.from_mapping(
        FROM_EMAIL=os.environ.get('FROM_EMAIL'),
        SENDGRID_KEY=os.environ.get('SENDGRID_API_KEY'),
        SECRET_KEY=os.environ.get('SECRET_KEY'),
        DATABASE_HOST=os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD=os.environ.get('FLASK_DATABSE_PASSWORD'),
        DATABASE_USER=os.environ.get('FLASK_DATABSE_USER'),
        DATABASE=os.environ.get('FLASK_DATABASE')
    )

    from . import db

    db.init_app(app)

    from . import mail

    app.register_blueprint(mail.bp)

    return app
