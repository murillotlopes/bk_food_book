from flask import Flask, Blueprint

bp_api = Blueprint('api', __name__, url_prefix='/api')


def init_app(app: Flask):

    app.register_blueprint(bp_api)