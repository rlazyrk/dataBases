from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import artists_events_connect_controller
from t08_flask_mysql.app.my_project.auth.domain.orders.artists_events_connect import ArtistsEventsConnect

artists_events_connect_bp = Blueprint('artists_events_connect', __name__, url_prefix='/artists_events_connect')


@artists_events_connect_bp.get('')
def get_all_artists_events_connect() -> Response:
    return make_response(jsonify(artists_events_connect_controller.find_all()), HTTPStatus.OK)


@artists_events_connect_bp.get('/<int:artists_events_connect_id>')
def get_artists_events_connect(artists_events_connect_id: int) -> Response:
    return make_response(jsonify(artists_events_connect_controller.find_by_id(artists_events_connect_id)),
                         HTTPStatus.OK)


@artists_events_connect_bp.post('')
def post_artists_events_connect() -> Response:
    json = request.get_json()
    artists_events_connect = ArtistsEventsConnect.create_from_dto(json)
    artists_events_connect_controller.create(artists_events_connect)
    return make_response(jsonify(artists_events_connect.put_into_dto()), HTTPStatus.OK)


@artists_events_connect_bp.put('/<int:artists_events_connect_id>')
def put_artists_events_connect(artists_events_connect_id: int) -> Response:
    json = request.get_json()
    order = ArtistsEventsConnect.create_from_dto(json)
    artists_events_connect_controller.update(artists_events_connect_id, order)
    return make_response("Order Updated", HTTPStatus.OK)


@artists_events_connect_bp.patch('/<int:artists_events_connect_id>')
def patch_artists_events_connect(artists_events_connect_id: int) -> Response:
    json = request.get_json()
    artists_events_connect_controller.patch(artists_events_connect_id, json)
    return make_response("Order Patched", HTTPStatus.OK)


@artists_events_connect_bp.delete('/<int:artists_events_connect_id>')
def delete_artists_events_connect(artists_events_connect_id: int) -> Response:
    artists_events_connect_controller.delete(artists_events_connect_id)
    return make_response("Order deleted", HTTPStatus.OK)
