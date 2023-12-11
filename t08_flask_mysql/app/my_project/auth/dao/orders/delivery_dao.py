from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain.orders.delivery import Delivery


class DeliveryDao(GeneralDAO):
    _domain_type = Delivery
