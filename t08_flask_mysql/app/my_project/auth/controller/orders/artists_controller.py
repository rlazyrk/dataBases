from t08_flask_mysql.app.my_project.auth.service import artists_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class ArtistsController(GeneralController):
    _service = artists_service
