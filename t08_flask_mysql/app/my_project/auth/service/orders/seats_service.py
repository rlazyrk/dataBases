from t08_flask_mysql.app.my_project.auth.dao import seats_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class SeatsService(GeneralService):
    _dao = seats_dao
