from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import orders_controller
from t08_flask_mysql.app.my_project.auth.domain.orders.orders import Orders

orders_bp = Blueprint('orders', __name__, url_prefix='/orders')


@orders_bp.get('')
def get_all_orders() -> Response:
    return make_response(jsonify(orders_controller.find_all()), HTTPStatus.OK)


@orders_bp.get('/<int:order_id>')
def get_order(order_id: int) -> Response:
    return make_response(jsonify(orders_controller.find_by_id(order_id)), HTTPStatus.OK)


@orders_bp.post('')
def post_order() -> Response:
    json = request.get_json()
    order = Orders.create_from_dto(json)
    orders_controller.create(order)
    return make_response(jsonify(order.put_into_dto()), HTTPStatus.OK)


@orders_bp.put('/<int:order_id>')
def put_order(order_id: int) -> Response:
    json = request.get_json()
    order = Orders.create_from_dto(json)
    orders_controller.update(order_id, order)
    return make_response("Order Updated", HTTPStatus.OK)


@orders_bp.patch('/<int:order_id>')
def patch_order(order_id: int) -> Response:
    json = request.get_json()
    orders_controller.patch(order_id, json)
    return make_response("Order Patched", HTTPStatus.OK)


@orders_bp.delete('/<int:order_id>')
def delete_order(order_id: int) -> Response:
    orders_controller.delete(order_id)
    return make_response("Order deleted", HTTPStatus.OK)

@orders_bp.get('/<string:operator>')
def get_min_max_avg_sum_of_cost(operator: str):
    print(orders_controller.get_min_max_avg_sum_of_cost(operator))
    return make_response(orders_controller.get_min_max_avg_sum_of_cost(operator),HTTPStatus.OK)