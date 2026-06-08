# MySQL Database Connection Example

import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD"
    )

    print("Connection successful.")
    print(mydb)

except Exception:
    print("An error occurred while connecting to the database.")
