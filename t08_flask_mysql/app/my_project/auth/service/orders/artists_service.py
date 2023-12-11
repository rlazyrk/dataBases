from t08_flask_mysql.app.my_project.auth.dao import artists_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class ArtistsService(GeneralService):
    _dao = artists_dao
    