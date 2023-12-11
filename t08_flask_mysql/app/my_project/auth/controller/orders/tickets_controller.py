from t08_flask_mysql.app.my_project.auth.service import ticket_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class TicketController(GeneralController):
    _service = ticket_service
