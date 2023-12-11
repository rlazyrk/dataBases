from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain.orders.places import Places


class PlacesDao(GeneralDAO):
    _domain_type = Places
