from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import tickets_controller
from t08_flask_mysql.app.my_project.auth.domain.orders.tickets import Tickets

tickets_bp = Blueprint('tickets', __name__, url_prefix='/tickets')


@tickets_bp.get('')
def get_all_tickets() -> Response:
    return make_response(jsonify(tickets_controller.find_all()), HTTPStatus.OK)


@tickets_bp.get('/<int:ticket_id>')
def get_ticket(ticket_id: int) -> Response:
    return make_response(jsonify(tickets_controller.find_by_id(ticket_id)), HTTPStatus.OK)


@tickets_bp.post('')
def post_ticket() -> Response:
    json = request.get_json()
    ticket = Tickets.create_from_dto(json)
    tickets_controller.create(ticket)
    return make_response(jsonify(ticket.put_into_dto()), HTTPStatus.OK)


@tickets_bp.put('/<int:ticket_id>')
def put_ticket(ticket_id: int) -> Response:
    json = request.get_json()
    ticket = Tickets.create_from_dto(json)
    tickets_controller.update(ticket_id, ticket)
    return make_response("Ticket Updated", HTTPStatus.OK)


@tickets_bp.patch('/<int:ticket_id>')
def patch_ticket(ticket_id: int) -> Response:
    json = request.get_json()
    tickets_controller.patch(ticket_id, json)
    return make_response("Ticket Patched", HTTPStatus.OK)


@tickets_bp.delete('/<int:ticket_id>')
def delete_ticket(ticket_id: int) -> Response:
    tickets_controller.delete(ticket_id)
    return make_response("Ticket deleted", HTTPStatus.OK)