from flask import Flask
# from flask.ext.mail import Mail
# from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug.utils import import_string

# mail = Mail()
# db = SQLAlchemy()

blueprints = [
    'myapp.main:main',
    'myapp.admin:admin',
]


def create_app(config=None, name=None):
    if config is None:
        import config
        _s = config
    else:
        _s = config
    if name is None:
        name = __name__

    app = Flask(__name__)
    app.config.from_object(config)

    # Load extensions
    # mail.init_app(app)
    # db.init_app(app)

    # Load blueprints
    for bp_name in blueprints:
        bp = import_string(bp_name)
        app.register_blueprint(bp)

    return app
