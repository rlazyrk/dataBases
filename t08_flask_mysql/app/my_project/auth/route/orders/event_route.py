from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import events_controller
from t08_flask_mysql.app.my_project.auth.domain.orders.events import Events

events_bp = Blueprint('events', __name__, url_prefix='/events')


@events_bp.get('')
def get_all_events() -> Response:
    return make_response(jsonify(events_controller.find_all()), HTTPStatus.OK)


@events_bp.get('/<int:event_id>')
def get_event(event_id: int) -> Response:
    return make_response(jsonify(events_controller.find_by_id(event_id)), HTTPStatus.OK)


@events_bp.post('')
def post_event() -> Response:
    json = request.get_json()
    event = Events.create_from_dto(json)
    events_controller.create(event)
    return make_response(jsonify(event.put_into_dto()), HTTPStatus.OK)


@events_bp.put('/<int:event_id>')
def put_event(event_id: int) -> Response:
    json = request.get_json()
    event = Events.create_from_dto(json)
    events_controller.update(event_id, event)
    return make_response("Event Updated", HTTPStatus.OK)


@events_bp.patch('/<int:event_id>')
def patch_event(event_id: int) -> Response:
    json = request.get_json()
    events_controller.patch(event_id, json)
    return make_response("Event Patched", HTTPStatus.OK)


@events_bp.delete('/<int:event_id>')
def delete_event(event_id: int) -> Response:
    events_controller.delete(event_id)
    return make_response("Event deleted", HTTPStatus.OK)