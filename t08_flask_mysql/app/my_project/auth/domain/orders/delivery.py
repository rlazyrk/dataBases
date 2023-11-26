from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Delivery(db.Model, IDto):
    __tablename__ = "delivery"

    idDelivery = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Delivery_cost = db.Column(db.DECIMAL, nullable=True)
    Delivery_address = db.Column(db.String(45), nullable=True)

    def __repr__(self):
        return f"Delivery({self.idDelivery}, {self.Delivery_cost}, `{self.Delivery_address}`)"

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> Delivery:
        obj = Delivery(
            Delivery_cost=dto_dict.get("Delivery_cost"),
            Delivery_address=dto_dict.get("Delivery_address")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "idDelivery": self.idDelivery,
            "Delivery_cost": self.Delivery_cost,
            "Delivery_address": self.Delivery_address
        }
