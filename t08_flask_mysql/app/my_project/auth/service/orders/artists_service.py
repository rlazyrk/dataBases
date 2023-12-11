from t08_flask_mysql.app.my_project.auth.dao import artists_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class ArtistsService(GeneralService):
    _dao = artists_dao

    def create_with_mtm_table(self, obj, events_id_list):
        return self._dao.create_with_mtm_table(obj, events_id_list)
