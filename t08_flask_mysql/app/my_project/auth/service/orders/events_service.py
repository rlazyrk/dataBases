from t08_flask_mysql.app.my_project.auth.dao import events_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class EventsService(GeneralService):
    _dao = events_dao
