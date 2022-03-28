from flask import Flask, Blueprint

from .recipe_route import bp as bp_route

bp_api = Blueprint('api', __name__, url_prefix='/api')


def init_app(app: Flask):

    bp_api.register_blueprint(bp_route)

    app.register_blueprint(bp_api)
