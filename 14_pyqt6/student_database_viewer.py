# Student Database Viewer using PyQt6 and MySQL

import sys
import mysql.connector

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QTableWidget,
    QTableWidgetItem
)


def get_students_from_db():

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD",
        database="school"
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            id,
            full_name,
            age,
            department
        FROM students
        """
    )

    students = cursor.fetchall()

    connection.close()

    return students


class StudentTable(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Student List")
        self.setGeometry(100, 100, 600, 300)

        layout = QVBoxLayout()

        self.table_widget = QTableWidget()

        self.table_widget.setColumnCount(4)

        self.table_widget.setHorizontalHeaderLabels(
            ["ID", "Full Name", "Age", "Department"]
        )

        students = get_students_from_db()

        self.populate_table(students)

        layout.addWidget(self.table_widget)

        self.setLayout(layout)

    def populate_table(self, students):

        self.table_widget.setRowCount(len(students))

        for row, student in enumerate(students):

            for column, value in enumerate(student):

                self.table_widget.setItem(
                    row,
                    column,
                    QTableWidgetItem(str(value))
                )


app = QApplication(sys.argv)

window = StudentTable()

window.show()

sys.exit(app.exec())
