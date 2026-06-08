# Select records using a parameterized query

import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="python_lessons"
)

cursor = connection.cursor()

sql = "SELECT * FROM students WHERE full_name = %s"

search_value = ("Esma SARI",)

cursor.execute(sql, search_value)

results = cursor.fetchall()

for row in results:
    print(row)
