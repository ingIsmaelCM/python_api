from peewee import MySQLDatabase
from app.configs.database import dbConfig

db=MySQLDatabase(dbConfig["dbName"], user=dbConfig["dbUser"], password=dbConfig["dbPassword"],
                 host="db", port=int(dbConfig["dbPort"]))


print(dbConfig["dbHost"])
def connect():
    try:
        return db.connect(True)
    except Exception as e:
        print(e)
        return e