from t08_flask_mysql.app.my_project.auth.dao import artists_events_connect_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class ArtistsEventConnectService(GeneralService):
    _dao = artists_events_connect_dao
