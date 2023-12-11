from t08_flask_mysql.app.my_project.auth.service import referral_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class ReferralsController(GeneralController):
    _service = referral_service
