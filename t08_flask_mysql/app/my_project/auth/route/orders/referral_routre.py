from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import referral_controller
from t08_flask_mysql.app.my_project.auth.domain.orders.referrals import Referrals

referrals_bp = Blueprint('referrals', __name__, url_prefix='/referrals')


@referrals_bp.get('')
def get_all_payments() -> Response:
    return make_response(jsonify(referral_controller.find_all()), HTTPStatus.OK)


@referrals_bp.get('/<int:referral_id>')
def get_payment(referral_id: int) -> Response:
    return make_response(jsonify(referral_controller.find_by_id(referral_id)), HTTPStatus.OK)


@referrals_bp.post('')
def post_payment() -> Response:
    json = request.get_json()
    referral = Referrals.create_from_dto(json)
    referral_controller.create(referral)
    return make_response(jsonify(referral.put_into_dto()), HTTPStatus.OK)


@referrals_bp.put('/<int:referral_id>')
def put_payment(referral_id: int) -> Response:
    json = request.get_json()
    referral = Referrals.create_from_dto(json)
    referral_controller.update(referral_id, referral)
    return make_response("Referral Updated", HTTPStatus.OK)


@referrals_bp.patch('/<int:referral_id>')
def patch_payment(referral_id: int) -> Response:
    json = request.get_json()
    referral_controller.patch(referral_id, json)
    return make_response("Referral Patched", HTTPStatus.OK)


@referrals_bp.delete('/<int:referral_id>')
def delete_payment(referral_id: int) -> Response:
    referral_controller.delete(referral_id)
    return make_response("Referral deleted", HTTPStatus.OK)