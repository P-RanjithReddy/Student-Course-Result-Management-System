import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "Ranju@123",
    "database": "student_management_db"
}

def get_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Database connection error: {e}")
    return None
if __name__ == "__main__":
    connection = get_connection()

    if connection:
        print("MySQL connection successful!")
        connection.close()
    else:
        print("MySQL connection failed!")