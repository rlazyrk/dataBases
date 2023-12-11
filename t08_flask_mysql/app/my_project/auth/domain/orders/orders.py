from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Orders(db.Model, IDto):
    __tablename__ = "orders"

    idOrders = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Users_idUsers = db.Column(db.Integer, db.ForeignKey('users.idUsers'), nullable=False)
    Order_date_time = db.Column(db.DateTime, nullable=False)
    Cost = db.Column(db.DECIMAL, nullable=False)
    Delivery_idDelivery = db.Column(db.Integer, db.ForeignKey('delivery.idDelivery'), nullable=False)

    user = db.relationship('Users', backref='orders')
    delivery = db.relationship('Delivery', backref='orders')

    def __repr__(self):
        return f"Order({self.idOrders}, {self.Users_idUsers}, `{self.Order_date_time}`, {self.Cost}, {self.Delivery_idDelivery})"

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> Orders:
        obj = Orders(
            Users_idUsers=dto_dict.get("Users_idUsers"),
            Order_date_time=dto_dict.get("Order_date_time"),
            Cost=dto_dict.get("Cost"),
            Delivery_idDelivery=dto_dict.get("Delivery_idDelivery")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "idOrders": self.idOrders,
            "Users_idUsers": self.Users_idUsers,
            "Order_date_time": self.Order_date_time,
            "Cost": self.Cost,
            "Delivery_idDelivery": self.Delivery_idDelivery
        }
