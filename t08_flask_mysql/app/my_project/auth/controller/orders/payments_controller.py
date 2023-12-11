from t08_flask_mysql.app.my_project.auth.service import payments_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class PaymentsController(GeneralController):
    _service = payments_service
