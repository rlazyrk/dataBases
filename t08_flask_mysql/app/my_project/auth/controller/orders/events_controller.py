from t08_flask_mysql.app.my_project.auth.service import events_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class EventsController(GeneralController):
    _service = events_service
