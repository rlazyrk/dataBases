from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Users(db.Model, IDto):
    __tablename__ = "users"

    idUsers = db.Column(db.Integer, primary_key=True, autoincrement=True)
    User_name = db.Column(db.String(45), nullable=False)
    User_lastname = db.Column(db.String(45), nullable=False)
    User_email = db.Column(db.String(45), nullable=False)
    User_phonenumber = db.Column(db.String(45), nullable=False)

    orders_user = db.relationship("Orders", backref="users")
    def __repr__(self):
        return f"User({self.idUsers}, `{self.User_name}`, `{self.User_lastname}`, `{self.User_email}`, `{self.User_phonenumber}`)"

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> Users:
        obj = Users(
            User_name=dto_dict.get("User_name"),
            User_lastname=dto_dict.get("User_lastname"),
            User_email=dto_dict.get("User_email"),
            User_phonenumber=dto_dict.get("User_phonenumber")
        )
        return obj

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "idUsers": self.idUsers,
            "User_name": self.User_name,
            "User_lastname": self.User_lastname,
            "User_email": self.User_email,
            "User_phonenumber": self.User_phonenumber,
            "Orders": [
                order.put_into_dto() for order in self.orders_user
            ]
        }
