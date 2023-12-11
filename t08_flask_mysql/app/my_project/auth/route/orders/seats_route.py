from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import seats_controller
from t08_flask_mysql.app.my_project.auth.domain.orders.seats import Seats

seats_bp = Blueprint('seats', __name__, url_prefix='/seats')


@seats_bp.get('')
def get_all_seats() -> Response:
    return make_response(jsonify(seats_controller.find_all()), HTTPStatus.OK)


@seats_bp.get('/<int:seat_id>')
def get_seat(seat_id: int) -> Response:
    return make_response(jsonify(seats_controller.find_by_id(seat_id)), HTTPStatus.OK)


@seats_bp.post('')
def post_seat() -> Response:
    json = request.get_json()
    seat = Seats.create_from_dto(json)
    seats_controller.create(seat)
    return make_response(jsonify(seat.put_into_dto()), HTTPStatus.OK)


@seats_bp.put('/<int:seat_id>')
def put_seat(seat_id: int) -> Response:
    json = request.get_json()
    seat = Seats.create_from_dto(json)
    seats_controller.update(seat_id, seat)
    return make_response("Seat Updated", HTTPStatus.OK)


@seats_bp.patch('/<int:seat_id>')
def patch_seat(seat_id: int) -> Response:
    json = request.get_json()
    seats_controller.patch(seat_id, json)
    return make_response("Seat Patched", HTTPStatus.OK)


@seats_bp.delete('/<int:seat_id>')
def delete_seat(seat_id: int) -> Response:
    seats_controller.delete(seat_id)
    return make_response("Seat deleted", HTTPStatus.OK)
