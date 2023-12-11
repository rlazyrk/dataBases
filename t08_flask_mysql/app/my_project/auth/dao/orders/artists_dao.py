import sqlalchemy

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain.orders.aritsts import Artists


class ArtistsDao(GeneralDAO):
    _domain_type = Artists

    def create_with_mtm_table(self, obj: object, events_id_list) -> object:
        self._session.add(obj)
        self._session.commit()
        artist_id = obj.idArtists
        for id in events_id_list:
            query = sqlalchemy.text("CALL ManyToManyConnectArtists_to_Events(:p1, :p2)")
            query = query.bindparams(p1=artist_id, p2=id)
            self._session.execute(query)
            self._session.commit()
        return obj
