import mysql.connector
from mysql.connector import Error

def get_database_connection():
    """Establishes a connection to the database."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="python"
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

def initialize_db():
    """Creates the employee table in the database if it doesn't exist."""
    try:
        connection = get_database_connection()
        if connection is not None:
            cur = connection.cursor()
            cur.execute(
                """CREATE TABLE IF NOT EXISTS employee(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    age INT NOT NULL,
                    department CHAR(50),
                    salary INT NOT NULL,
                    managed_department CHAR(50) DEFAULT NULL
                    );"""   
            )
            connection.commit()
    except Error as e:
        print(f"Error creating database table: {e}")
    finally:
        if connection:
            connection.close()