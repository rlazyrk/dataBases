from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import artists_controller
from t08_flask_mysql.app.my_project.auth.domain.orders.aritsts import Artists

artists_bp = Blueprint('artist', __name__, url_prefix='/artists')


@artists_bp.get('')
def get_all_artists() -> Response:
    return make_response(jsonify(artists_controller.find_all()), HTTPStatus.OK)


@artists_bp.get('/<int:artists_id>')
def get_artist(artists_id: int) -> Response:
    return make_response(jsonify(artists_controller.find_by_id(artists_id)), HTTPStatus.OK)


@artists_bp.post('')
def post_artists() -> Response:
    json = request.get_json()
    artist = Artists.create_from_dto(json)
    artists_controller.create(artist)
    return make_response(jsonify(artist.put_into_dto()), HTTPStatus.OK)


@artists_bp.put('/<int:artists_id>')
def put_artists(artists_id: int) -> Response:
    json = request.get_json()
    artist = Artists.create_from_dto(json)
    artists_controller.update(artists_id, artist)
    return make_response("Artist Updated", HTTPStatus.OK)


@artists_bp.patch('/<int:artists_id>')
def patch_artists(artists_id: int) -> Response:
    json = request.get_json()
    artists_controller.patch(artists_id, json)
    return make_response("Artist Patched", HTTPStatus.OK)


@artists_bp.delete('/<int:artists_id>')
def delete_artist(artists_id: int) -> Response:
    artists_controller.delete(artists_id)
    return make_response("Artist deleted", HTTPStatus.OK)
