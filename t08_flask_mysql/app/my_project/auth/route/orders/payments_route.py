from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import payments_controller
from t08_flask_mysql.app.my_project.auth.domain.orders.payments import Payments  # Переконайтеся, що ви імпортуєте правильну модель Payments

payments_bp = Blueprint('payments', __name__, url_prefix='/payments')


@payments_bp.get('')
def get_all_payments() -> Response:
    return make_response(jsonify(payments_controller.find_all()), HTTPStatus.OK)


@payments_bp.get('/<int:payment_id>')
def get_payment(payment_id: int) -> Response:
    return make_response(jsonify(payments_controller.find_by_id(payment_id)), HTTPStatus.OK)


@payments_bp.post('')
def post_payment() -> Response:
    json = request.get_json()
    payment = Payments.create_from_dto(json)
    payments_controller.create(payment)
    return make_response(jsonify(payment.put_into_dto()), HTTPStatus.OK)


@payments_bp.put('/<int:payment_id>')
def put_payment(payment_id: int) -> Response:
    json = request.get_json()
    payment = Payments.create_from_dto(json)
    payments_controller.update(payment_id, payment)
    return make_response("Payment Updated", HTTPStatus.OK)


@payments_bp.patch('/<int:payment_id>')
def patch_payment(payment_id: int) -> Response:
    json = request.get_json()
    payments_controller.patch(payment_id, json)
    return make_response("Payment Patched", HTTPStatus.OK)


@payments_bp.delete('/<int:payment_id>')
def delete_payment(payment_id: int) -> Response:
    payments_controller.delete(payment_id)
    return make_response("Payment deleted", HTTPStatus.OK)