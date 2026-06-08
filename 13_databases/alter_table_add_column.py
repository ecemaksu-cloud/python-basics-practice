# Add a new column to an existing table

import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="python_lessons"
)

cursor = connection.cursor()

cursor.execute(
    "ALTER TABLE students ADD COLUMN national_id VARCHAR(11)"
)

print("Column added successfully.")

connection.commit()
