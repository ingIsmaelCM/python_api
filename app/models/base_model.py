from app.models.connection import db
from peewee import Model


class BaseModel(Model):
    class Meta:
        database= db
