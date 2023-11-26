from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Artists(db.Model, IDto):
    __tablename__ = "artists"

    idArtists = db.Column(db.Integer, primary_key=True, autoincrement=True)
    genre = db.Column(db.String(45), nullable=False)
    artist_name = db.Column(db.String(45), nullable=False)

    def __repr__(self):
        return f"Artist({self.idArtists}, `{self.artist_name}`, `{self.genre}`)"

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> Artists:
        obj = Artists(
            genre=dto_dict.get("genre"),
            artist_name=dto_dict.get("artist_name"),
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.idArtists,
            "genre": self.genre,
            "artist_name": self.artist_name
        }
