from t08_flask_mysql.app.my_project.auth.service import user_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class UsersController(GeneralController):
    _service = user_service
