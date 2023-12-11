from t08_flask_mysql.app.my_project.auth.service import artists_events_connect_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class ArtistsEventConnectController(GeneralController):
    _service = artists_events_connect_service
