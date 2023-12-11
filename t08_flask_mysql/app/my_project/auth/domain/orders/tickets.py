from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Tickets(db.Model, IDto):
    __tablename__ = "tickets"

    idTickets = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Orders_idOrders = db.Column(db.Integer, db.ForeignKey('orders.idOrders'), nullable=False)
    Events_idevent = db.Column(db.Integer, db.ForeignKey('events.idevent'), nullable=False)
    Seats_idSeats = db.Column(db.Integer, db.ForeignKey('seats.idSeats'), nullable=False)

    order = db.relationship('Orders', backref='tickets', foreign_keys=[Orders_idOrders])
    event = db.relationship('Events', backref='tickets', foreign_keys=[Events_idevent])
    seat = db.relationship('Seats', backref='tickets', foreign_keys=[Seats_idSeats])

    def __repr__(self):
        return f"Ticket({self.idTickets}, {self.Orders_idOrders}, {self.Events_idevent}, {self.Seats_idSeats})"

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> Tickets:
        obj = Tickets(
            Orders_idOrders=dto_dict.get("Orders_idOrders"),
            Events_idevent=dto_dict.get("Events_idevent"),
            Seats_idSeats=dto_dict.get("Seats_idSeats"),
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "idTickets": self.idTickets,
            "Order": {
                "idOrders": self.order.idOrders,
                "Users_idUsers": self.order.Users_idUsers,
                "Order_date_time": self.order.Order_date_time,
                "Cost": self.order.Cost,
                "Delivery_idDelivery": self.order.Delivery_idDelivery
            },
            "Event": {
                "idevent": self.event.idevent,
                "eventname": self.event.eventname,
                "datetime": self.event.datetime,
            },
            "Seat": {
                "idSeats": self.seat.idSeats,
                "Places_idPlaces": self.seat.Places_idPlaces,
                "row": self.seat.row,
                "seat_number": self.seat.seat_number,
            },
        }
