# Simple math quiz game

import random

questions = {
    "5 + 3 = ?": 8,
    "7 - 2 = ?": 5,
    "4 * 2 = ?": 8
}

while True:
    question = random.choice(list(questions.keys()))

    answer = int(input(question + " "))

    if answer == questions[question]:
        print("Correct!")
        break
    else:
        print("Wrong answer. Try again.")
