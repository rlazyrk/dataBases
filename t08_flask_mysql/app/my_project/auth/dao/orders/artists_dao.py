from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain.orders.aritsts import Artists


class ArtistsDao(GeneralDAO):
    _domain_type = Artists
