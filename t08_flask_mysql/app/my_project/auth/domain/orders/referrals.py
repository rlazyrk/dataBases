from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Referrals(db.Model, IDto):
    __tablename__ = "referrals"

    referral_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer,nullable=False)
    referral_name = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"Referrals({self.referral_id}, {self.user_id}, `{self.referral_name}`)"

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> Referrals:
        obj = Referrals(
            user_id=dto_dict.get("user_id"),
            referral_name=dto_dict.get("referral_name")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "referral_id": self.referral_id,
            "user_id": self.user_id,
            "referral_name": self.referral_name,
        }