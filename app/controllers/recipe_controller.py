from http import HTTPStatus
from flask import jsonify, request
from app.models.recipe_model import Recipes


def recipes_get_page():

    page = int(request.args.get('page'))

    data = list(Recipes.recipes_get_page(page))

    if not data:
        return {'msg': 'Não há informações para retorno'}, HTTPStatus.NOT_FOUND

    for d in data:
        d.update({'_id': str(d['_id'])})


    if len(data) > 10:
        nextPage = page + 1
        data.pop()
    else:
        nextPage = None

    return {
        'nextPage': nextPage,
        'data': data
    }, HTTPStatus.OK
