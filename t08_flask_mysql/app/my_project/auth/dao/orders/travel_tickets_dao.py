from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain.orders.travel_tickets import TravelTickets


class TravelTicketsDao(GeneralDAO):
    _domain_type = TravelTickets
