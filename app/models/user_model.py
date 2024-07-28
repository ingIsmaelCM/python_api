from app.models.base_model import BaseModel
from peewee import *


class UserModel(BaseModel):
    class Meta:
        table_name = "users"

    id = UUIDField(primary_key=True, unique=True)
    username = CharField(unique=True)
    password = CharField()
    email = CharField()
    