import mysql.connector
from secret import get_secret

def get_connection():
    return mysql.connector.connect(
        host = "10.0.1.97",
        user = "guillaume",
        password = get_secret(),
        database = "webapp"
    )