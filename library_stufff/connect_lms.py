import mysql.connector
from mysql.connector import Error
def connect_db():
    db_name= "lmsdatabase_"
    user = "root"
    password = "Von&Drea0823"
    host = "localhost"

    try:
        conn = mysql.connector.connect(
            database = db_name,
            user=user,
            password=password,
            host=host
        )
        if conn.is_connected():
            print(":)")
            return conn

    except Error as e:
        print(f"Error: {e}")
connect_db()