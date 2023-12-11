import sqlalchemy

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain.orders.users import Users


class UsersDao(GeneralDAO):
    _domain_type = Users

    def parameter_insert_user(self, name, last_name, email, phonenumber):
        query = sqlalchemy.text("CALL ParameterInsertUser(:p1, :p2, :p3, :p4)")
        query = query.bindparams(p1=name, p2=last_name, p3=email, p4=phonenumber)

        self._session.execute(query)
        self._session.commit()

    def generate_default_user(self, name):
        query = sqlalchemy.text("CALL GeneratedUsersInsert(:p1)")
        query = query.bindparams(p1=name)

        self._session.execute(query)
        self._session.commit()

