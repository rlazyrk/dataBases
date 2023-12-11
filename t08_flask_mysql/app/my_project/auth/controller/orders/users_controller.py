from t08_flask_mysql.app.my_project.auth.service import user_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class UsersController(GeneralController):
    _service = user_service

    def parameter_insert_user(self, name, last_name, email, phonenumber):
        self._service.parameter_insert_user(name, last_name, email, phonenumber)

    def generate_default_user(self, name):
        self._service.generate_default_user(name)
