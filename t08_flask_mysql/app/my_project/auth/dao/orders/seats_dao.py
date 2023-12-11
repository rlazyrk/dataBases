from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain.orders.seats import Seats


class SeatsDao(GeneralDAO):
    _domain_type = Seats
