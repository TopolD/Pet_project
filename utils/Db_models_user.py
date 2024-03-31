from typing import Annotated
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from utils.Db import Base

intpk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]

""" Модели по чату """


class user(Base):
    __tablename__ = "user"
    ID: Mapped[intpk]
    image: Mapped[str]
    username: Mapped[int] = mapped_column(nullable=False)
    in_offer: Mapped[str] = mapped_column(default='0')
    in_admin: Mapped[str] = mapped_column(default='0')
    Auth_id: Mapped[int]
    countries = mapped_column(ForeignKey('countries.ID'))
    hobby = mapped_column(ForeignKey('hobby.ID'))

    def __init__(self, image=None, username=None):
        self.image = image
        self.username = username


class hobby(Base):
    __tablename__ = "hobby"
    ID: Mapped[intpk]
    Hobby_name: Mapped[str]


class countries(Base):
    __tablename__ = "countries"
    ID: Mapped[intpk]
    label: Mapped[str]


class chat(Base):
    __tablename__ = "chat"
    ID: Mapped[intpk]
    name: Mapped[str]
    messages: Mapped[str]
