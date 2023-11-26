from t08_flask_mysql.app.my_project.auth.dao import tickets_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class TicketsService(GeneralService):
    _dao = tickets_dao
