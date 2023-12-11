from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import places_controller
from t08_flask_mysql.app.my_project.auth.domain.orders.places import Places

places_bp = Blueprint('places', __name__, url_prefix='/places')


@places_bp.get('')
def get_all_places() -> Response:
    return make_response(jsonify(places_controller.find_all()), HTTPStatus.OK)


@places_bp.get('/<int:place_id>')
def get_place(place_id: int) -> Response:
    return make_response(jsonify(places_controller.find_by_id(place_id)), HTTPStatus.OK)


@places_bp.post('')
def post_place() -> Response:
    json = request.get_json()
    place = Places.create_from_dto(json)
    places_controller.create(place)
    return make_response(jsonify(place.put_into_dto()), HTTPStatus.OK)


@places_bp.put('/<int:place_id>')
def put_place(place_id: int) -> Response:
    json = request.get_json()
    place = Places.create_from_dto(json)
    places_controller.update(place_id, place)
    return make_response("Place Updated", HTTPStatus.OK)


@places_bp.patch('/<int:place_id>')
def patch_place(place_id: int) -> Response:
    json = request.get_json()
    places_controller.patch(place_id, json)
    return make_response("Place Patched", HTTPStatus.OK)


@places_bp.delete('/<int:place_id>')
def delete_place(place_id: int) -> Response:
    places_controller.delete(place_id)
    return make_response("Place deleted", HTTPStatus.OK)


@places_bp.get('/separate/<string:name1>/<string:name2>')
def separate(name1: str, name2: str):
    places_controller.separate(name1, name2)
    return make_response(" ", HTTPStatus.OK)
