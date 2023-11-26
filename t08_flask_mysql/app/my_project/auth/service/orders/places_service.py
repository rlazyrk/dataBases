from t08_flask_mysql.app.my_project.auth.dao import places_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class PlacesService(GeneralService):
    _dao = places_dao
