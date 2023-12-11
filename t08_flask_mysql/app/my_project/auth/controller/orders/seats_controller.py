from t08_flask_mysql.app.my_project.auth.service import seats_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class SeatsController(GeneralController):
    _service = seats_service
