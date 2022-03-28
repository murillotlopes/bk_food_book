from flask import Blueprint
from app.controllers import recipe_controller


bp = Blueprint('recipes', __name__, url_prefix='/recipes')


bp.get('')(recipe_controller.recipes_get_page)
