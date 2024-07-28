import os
import typing

dbConfig: typing.Dict[str, str] = {
    "dbName": os.getenv("DATABASE_NAME"),
    "dbUser": os.getenv("DATABASE_USER"),
    "dbPassword": os.getenv("DATABASE_PASSWORD"),
    "dbHost": os.getenv('DATABASE_HOST'),
    "dbPort": os.getenv("DATABASE_PORT")

}