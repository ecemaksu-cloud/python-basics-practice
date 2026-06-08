# Create and list MySQL databases

import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD"
    )

    print("Connection successful.")
    print(connection)

    try:
        cursor = connection.cursor()

        cursor.execute(
            "CREATE DATABASE python_lessons"
        )

        print("Database created successfully.")

    except mysql.connector.Error as error:
        print(
            f"Database could not be created. Error: {error}"
        )

except Exception:
    print("An error occurred during the process.")


# List all databases

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD"
)

cursor = connection.cursor()

cursor.execute("SHOW DATABASES")

for database in cursor:
    print(database)
