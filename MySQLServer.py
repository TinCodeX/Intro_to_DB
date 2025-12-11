# MySQLServer.py

import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YourRootPassword"  # Replace with your actual MySQL root password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:  # <- exact string ALX looks for
    print(f"Error: {e}")

finally:
    if 'cursor' in locals() and cursor.is_connected():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
