from t08_flask_mysql.app.my_project.auth.service import delivery_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class DeliveryController(GeneralController):
    _service = delivery_service
