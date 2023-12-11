import sqlalchemy

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain.orders.places import Places


class PlacesDao(GeneralDAO):
    _domain_type = Places

    def separate(self, name1: str, name2: str):
        query = sqlalchemy.text("CALL CursorProcedureFirstTask(:p1, :p2)")
        query = query.bindparams(p1=name1, p2=name2)
        self._session.execute(query)
        self._session.commit()
