from typing import List
from .user_abstract import AbstractRepository


fake_db = {"id": 1, "name": "Cainã Moara", "email": "cainamoara@example.com"}


class UserRepository(AbstractRepository):

    def __init__(self):
        super().__init__()

    @staticmethod
    def select():
        return fake_db
