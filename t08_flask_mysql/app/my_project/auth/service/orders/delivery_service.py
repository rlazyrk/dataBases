from t08_flask_mysql.app.my_project.auth.dao import delivery_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class DeliveryService(GeneralService):
    _dao = delivery_dao
