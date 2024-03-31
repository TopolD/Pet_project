# from sqlalchemy.testing.pickleable import User
from .Db_models_user import user

from utils import Db

"""Регистрация\вход пользователя """


def GetInUser(username: str):
    Db.init_db()
    Users = Db.db_session.query(user).all().dict()
    User = [User for User in Users]
    if User == username:
        pass

    else:
        pass
