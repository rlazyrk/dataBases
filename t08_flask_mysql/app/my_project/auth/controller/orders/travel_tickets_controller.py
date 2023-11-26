from t08_flask_mysql.app.my_project.auth.service import travel_ticket_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class TravelTicketController(GeneralController):
    _service = travel_ticket_service
