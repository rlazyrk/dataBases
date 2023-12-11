import sqlalchemy

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain.orders.orders import Orders


class OrdersDao(GeneralDAO):
    _domain_type = Orders

    def get_min_max_avg_sum_of_cost(self, operator) -> object:
        query = sqlalchemy.text("CALL MinMaxAvgSumOrdersCost(:p1, @result)")
        query = query.bindparams(p1=operator)
        result = self._session.execute(query)
        result_value = self._session.query(sqlalchemy.literal_column('@result').label('result')).first()
        return str(result_value.result)

