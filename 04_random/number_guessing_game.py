# Number guessing game

import random

secret_number = random.randint(10, 30)

guess = 0
attempts = 0

while guess != secret_number:
    guess = int(input("Guess a number between 10 and 30: "))
    attempts += 1

    if guess < secret_number:
        print("Try a larger number.")
    elif guess > secret_number:
        print("Try a smaller number.")
    else:
        print("You found the number in", attempts, "attempts.")
