# MySQLServer.py

import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='your_root_password'  # Replace with your root password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        
        # Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error: {e}")

finally:
    # Close cursor and connection
    if 'cursor' in locals() and cursor.is_connected():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
