from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Seats(db.Model, IDto):
    __tablename__ = "seats"

    idSeats = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Places_idPlaces = db.Column(db.Integer, db.ForeignKey('places.idPlaces'), nullable=False)
    row = db.Column(db.Integer, nullable=False)
    seat_number = db.Column(db.Integer, nullable=False)
    free = db.Column(db.Boolean, nullable=False)
    place = db.relationship('Places', backref='seats_ref')

    def __repr__(self):
        return f"Seat({self.idSeats}, {self.Places_idPlaces}, {self.row}, {self.seat_number}, {self.free})"

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> Seats:
        obj = Seats(
            Places_idPlaces=dto_dict.get("Places_idPlaces"),
            row=dto_dict.get("row"),
            seat_number=dto_dict.get("seat_number"),
            free=dto_dict.get("free")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "idSeats": self.idSeats,
            "Places_idPlaces": self.Places_idPlaces,
            "row": self.row,
            "seat_number": self.seat_number,
            "free": self.free
        }
