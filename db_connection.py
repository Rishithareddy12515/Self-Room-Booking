# db_connection.py

import mysql.connector

def connect_to_database():
    connection = mysql.connector.connect(
        host="localhost",     
        user="root",
        password="rishi@2005",
        database="room_booking"
    )
    return connection

