# Student Table Application using PyQt6

import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QTableWidget,
    QTableWidgetItem
)


class StudentTable(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Student List")
        self.setGeometry(100, 100, 500, 300)

        layout = QVBoxLayout()

        self.table_widget = QTableWidget()

        self.table_widget.setColumnCount(4)

        self.table_widget.setHorizontalHeaderLabels(
            ["ID", "Full Name", "Age", "Department"]
        )

        students = [
            (1, "Ali Yilmaz", 20, "Computer Engineering"),
            (2, "Ayse Kaya", 22, "Mechanical Engineering"),
            (3, "Mehmet Demir", 21, "Electrical Engineering"),
            (4, "Zeynep Arslan", 23, "Civil Engineering")
        ]

        self.populate_table(students)

        layout.addWidget(self.table_widget)

        self.setLayout(layout)

    def populate_table(self, students):

        self.table_widget.setRowCount(len(students))

        for row, student in enumerate(students):

            for col, data in enumerate(student):

                self.table_widget.setItem(
                    row,
                    col,
                    QTableWidgetItem(str(data))
                )


app = QApplication(sys.argv)

window = StudentTable()

window.show()

sys.exit(app.exec())
