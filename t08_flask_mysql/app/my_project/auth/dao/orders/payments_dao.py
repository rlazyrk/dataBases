from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain.orders.payments import Payments


class PaymentsDao(GeneralDAO):
    _domain_type = Payments
