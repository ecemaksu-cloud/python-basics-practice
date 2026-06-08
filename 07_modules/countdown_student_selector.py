# Random student selection with countdown

import random
import time

students = ["Ayse", "Okan", "Fatma", "Hamza", "Ela", "Okyay"]

selected_student = random.choice(students)

countdown = 5

while countdown > 0:
    print(countdown)
    time.sleep(1)
    countdown -= 1

print("Time is up!")
print("Selected student:", selected_student)
