from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto

class TravelTickets(db.Model, IDto):
    __tablename__ = "traveltickets"

    idTravelTickets = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Orders_idOrders = db.Column(db.Integer, db.ForeignKey('orders.idOrders'), nullable=False)
    Transport_type = db.Column(db.String(45), nullable=False)
    Cost = db.Column(db.DECIMAL, nullable=False)
    Date_time = db.Column(db.DateTime, nullable=False)

    order = db.relationship('Orders', backref='traveltickets')

    def __repr__(self):
        return f"TravelTicket({self.idTravelTickets}, {self.Orders_idOrders}, `{self.Transport_type}`, {self.Cost}, `{self.Date_time}`)"

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> TravelTickets:
        obj = TravelTickets(
            Orders_idOrders=dto_dict.get("Orders_idOrders"),
            Transport_type=dto_dict.get("Transport_type"),
            Cost=dto_dict.get("Cost"),
            Date_time=dto_dict.get("Date_time")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "idTravelTickets": self.idTravelTickets,
            "Orders_idOrders": self.Orders_idOrders,
            "Transport_type": self.Transport_type,
            "Cost": self.Cost,
            "Date_time": self.Date_time
        }
