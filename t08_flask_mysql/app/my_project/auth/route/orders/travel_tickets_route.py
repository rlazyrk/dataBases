from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import travel_tickets_controller
from t08_flask_mysql.app.my_project.auth.domain.orders.travel_tickets import TravelTickets

travel_tickets_bp = Blueprint('travel_tickets', __name__, url_prefix='/travel_tickets')


@travel_tickets_bp.get('')
def get_all_travel_tickets() -> Response:
    return make_response(jsonify(travel_tickets_controller.find_all()), HTTPStatus.OK)


@travel_tickets_bp.get('/<int:travel_ticket_id>')
def get_travel_ticket(travel_ticket_id: int) -> Response:
    return make_response(jsonify(travel_tickets_controller.find_by_id(travel_ticket_id)), HTTPStatus.OK)


@travel_tickets_bp.post('')
def post_travel_ticket() -> Response:
    json = request.get_json()
    travel_ticket = TravelTickets.create_from_dto(json)
    travel_tickets_controller.create(travel_ticket)
    return make_response(jsonify(travel_ticket.put_into_dto()), HTTPStatus.OK)


@travel_tickets_bp.put('/<int:travel_ticket_id>')
def put_travel_ticket(travel_ticket_id: int) -> Response:
    json = request.get_json()
    travel_ticket = TravelTickets.create_from_dto(json)
    travel_tickets_controller.update(travel_ticket_id, travel_ticket)
    return make_response("Travel Ticket Updated", HTTPStatus.OK)


@travel_tickets_bp.patch('/<int:travel_ticket_id>')
def patch_travel_ticket(travel_ticket_id: int) -> Response:
    json = request.get_json()
    travel_tickets_controller.patch(travel_ticket_id, json)
    return make_response("Travel Ticket Patched", HTTPStatus.OK)


@travel_tickets_bp.delete('/<int:travel_ticket_id>')
def delete_travel_ticket(travel_ticket_id: int) -> Response:
    travel_tickets_controller.delete(travel_ticket_id)
    return make_response("Travel Ticket deleted", HTTPStatus.OK)
