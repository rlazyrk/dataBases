from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db


class ArtistsEventsConnect(db.Model):
    __tablename__ = "artists_events_connect"

    id_connection = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Artists_idArtists = db.Column(db.Integer, db.ForeignKey('artists.idArtists'))
    Events_idevent = db.Column(db.Integer, db.ForeignKey('events.idevent'))

    def __repr__(self):
        return f"ArtistsEventsConnect({self.Artists_idArtists}, {self.Events_idevent})"

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> ArtistsEventsConnect:
        obj = ArtistsEventsConnect(
            Artists_idArtists=dto_dict.get("Artists_idArtists"),
            Events_idevent=dto_dict.get("Events_idevent")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "Artists_idArtists": self.Artists_idArtists,
            "Events_idevent": self.Events_idevent
        }
