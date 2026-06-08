# Update a record in MySQL

import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="python_lessons"
)

cursor = connection.cursor()

sql = """
UPDATE customers
SET phone_number = %s
WHERE phone_number = %s
"""

values = (
    "05415556677",
    "05415236541"
)

cursor.execute(sql, values)

connection.commit()

print(cursor.rowcount, "record(s) updated.")
