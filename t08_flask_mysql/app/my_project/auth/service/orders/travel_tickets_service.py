from t08_flask_mysql.app.my_project.auth.dao import travel_tickets_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class TravelTicketsService(GeneralService):
    _dao = travel_tickets_dao
