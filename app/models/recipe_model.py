from app.models import db

class Recipes():

    @staticmethod
    def recipes_get_page(page: int):

        return db.recipes.find().limit(11).skip((page - 1) * 10)
