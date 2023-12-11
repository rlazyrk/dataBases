from t08_flask_mysql.app.my_project.auth.dao import users_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class UsersService(GeneralService):
    _dao = users_dao

    def parameter_insert_user(self, name, last_name, email, phonenumber):
        self._dao.parameter_insert_user(name, last_name, email, phonenumber)

    def generate_default_user(self, name):
        self._dao.generate_default_user(name)
