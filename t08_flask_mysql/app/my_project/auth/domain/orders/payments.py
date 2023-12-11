from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Payments(db.Model, IDto):
    __tablename__ = "payments"

    idPayments = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Orders_idOrders = db.Column(db.Integer, db.ForeignKey('orders.idOrders'), nullable=False)
    Payment_status = db.Column(db.String(45), nullable=False)

    order = db.relationship('Orders', backref='payments')

    def __repr__(self):
        return f"Payment({self.idPayments}, {self.Orders_idOrders}, `{self.Payment_status}`)"

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> Payments:
        obj = Payments(
            Orders_idOrders=dto_dict.get("Orders_idOrders"),
            Payment_status=dto_dict.get("Payment_status")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "idPayments": self.idPayments,
            "Orders_idOrders": self.Orders_idOrders,
            "Payment_status": self.Payment_status
        }
