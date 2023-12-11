from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain.orders.artists_events_connect import ArtistsEventsConnect


class ArtistsEventsConnectDao(GeneralDAO):
    _domain_type = ArtistsEventsConnect
