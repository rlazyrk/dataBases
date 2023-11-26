from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import users_controller
from t08_flask_mysql.app.my_project.auth.domain.orders.users import Users

users_bp = Blueprint('users', __name__, url_prefix='/users')


@users_bp.get('')
def get_all_users() -> Response:
    return make_response(jsonify(users_controller.find_all()), HTTPStatus.OK)


@users_bp.get('/<int:user_id>')
def get_user(user_id: int) -> Response:
    return make_response(jsonify(users_controller.find_by_id(user_id)), HTTPStatus.OK)


@users_bp.post('')
def post_user() -> Response:
    json = request.get_json()
    user = Users.create_from_dto(json)
    users_controller.create(user)
    return make_response(jsonify(user.put_into_dto()), HTTPStatus.OK)


@users_bp.put('/<int:user_id>')
def put_user(user_id: int) -> Response:
    json = request.get_json()
    user = Users.create_from_dto(json)
    users_controller.update(user_id, user)
    return make_response("User Updated", HTTPStatus.OK)


@users_bp.patch('/<int:user_id>')
def patch_user(user_id: int) -> Response:
    json = request.get_json()
    users_controller.patch(user_id, json)
    return make_response("User Patched", HTTPStatus.OK)


@users_bp.delete('/<int:user_id>')
def delete_user(user_id: int) -> Response:
    users_controller.delete(user_id)
    return make_response("User deleted", HTTPStatus.OK)
