from t08_flask_mysql.app.my_project.auth.service import orders_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class OrdersController(GeneralController):
    _service = orders_service
