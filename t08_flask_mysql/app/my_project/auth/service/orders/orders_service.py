from t08_flask_mysql.app.my_project.auth.dao import orders_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class OrdersService(GeneralService):
    _dao = orders_dao
