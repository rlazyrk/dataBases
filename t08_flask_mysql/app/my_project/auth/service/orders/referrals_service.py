from t08_flask_mysql.app.my_project.auth.dao import referrals_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class ReferralsService(GeneralService):
    _dao = referrals_dao
