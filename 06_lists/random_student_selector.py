# Random student selector

import random

students = ["Ayse", "Okan", "Fatma", "Hamza", "Ela", "Okyay"]

while True:
    selected_student = random.choice(students)

    print("Selected student:", selected_student)

    answer = input("Select again? (y/n): ")

    if answer.lower() == "n":
        print("Program ended.")
        break
