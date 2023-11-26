from t08_flask_mysql.app.my_project.auth.dao import payments_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class PaymentsService(GeneralService):
    _dao = payments_dao
