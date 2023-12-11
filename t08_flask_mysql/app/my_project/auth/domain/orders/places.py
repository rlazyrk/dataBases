from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Places(db.Model, IDto):
    __tablename__ = "places"

    idPlaces = db.Column(db.Integer, primary_key=True, autoincrement=True)
    addresses = db.Column(db.String(45), nullable=False)
    Place_name = db.Column(db.String(45), nullable=False)

    def __repr__(self):
        return f"Place({self.idPlaces}, `{self.addresses}`, `{self.Place_name}`)"

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> Places:
        obj = Places(
            addresses=dto_dict.get("addresses"),
            Place_name=dto_dict.get("Place_name"),
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "idPlaces": self.idPlaces,
            "addresses": self.addresses,
            "Place_name": self.Place_name
        }
