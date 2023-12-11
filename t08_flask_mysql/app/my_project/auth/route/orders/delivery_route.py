from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import delivery_controller
from t08_flask_mysql.app.my_project.auth.domain.orders.delivery import Delivery

delivery_bp = Blueprint('delivery', __name__, url_prefix='/delivery')


@delivery_bp.get('')
def get_all_deliveries() -> Response:
    return make_response(jsonify(delivery_controller.find_all()), HTTPStatus.OK)


@delivery_bp.get('/<int:delivery_id>')
def get_delivery(delivery_id: int) -> Response:
    return make_response(jsonify(delivery_controller.find_by_id(delivery_id)), HTTPStatus.OK)


@delivery_bp.post('')
def post_delivery() -> Response:
    json = request.get_json()
    delivery = Delivery.create_from_dto(json)
    delivery_controller.create(delivery)
    return make_response(jsonify(delivery.put_into_dto()), HTTPStatus.OK)


@delivery_bp.put('/<int:delivery_id>')
def put_delivery(delivery_id: int) -> Response:
    json = request.get_json()
    delivery = Delivery.create_from_dto(json)
    delivery_controller.update(delivery_id, delivery)
    return make_response("Delivery Updated", HTTPStatus.OK)


@delivery_bp.patch('/<int:delivery_id>')
def patch_delivery(delivery_id: int) -> Response:
    json = request.get_json()
    delivery_controller.patch(delivery_id, json)
    return make_response("Delivery Patched", HTTPStatus.OK)


@delivery_bp.delete('/<int:delivery_id>')
def delete_delivery(delivery_id: int) -> Response:
    delivery_controller.delete(delivery_id)
    return make_response("Delivery deleted", HTTPStatus.OK)