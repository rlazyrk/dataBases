from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain.orders.orders import Orders


class OrdersDao(GeneralDAO):
    _domain_type = Orders
