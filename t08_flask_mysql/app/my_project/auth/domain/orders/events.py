from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Events(db.Model, IDto):
    __tablename__ = "events"

    idevent = db.Column(db.Integer, primary_key=True, autoincrement=True)
    eventname = db.Column(db.String(45), nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)
    Places_idPlaces = db.Column(db.Integer, db.ForeignKey('places.idPlaces'), nullable=False)

    place = db.relationship('Places', backref="events")

    def __repr__(self):
        return f"Event({self.idevent}, `{self.eventname}`, `{self.datetime}`, {self.Places_idPlaces})"

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> Events:
        obj = Events(
            eventname=dto_dict.get("eventname"),
            datetime=dto_dict.get("datetime"),
            Places_idPlaces=dto_dict.get("Places_idPlaces")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "idevent": self.idevent,
            "eventname": self.eventname,
            "datetime": self.datetime,
            "Places_idPlaces": self.Places_idPlaces
        }
