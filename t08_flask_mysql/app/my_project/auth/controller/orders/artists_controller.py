from t08_flask_mysql.app.my_project.auth.service import artists_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class ArtistsController(GeneralController):
    _service = artists_service

    def create_with_mtm_table(self, obj: object, events_id_list: list) -> object:
        return self._service.create_with_mtm_table(obj, events_id_list).put_into_dto()