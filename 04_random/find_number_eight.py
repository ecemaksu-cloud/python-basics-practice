# Generate random numbers until 8 appears

import random

attempts = 0

while True:
    number = random.randint(5, 21)

    print("Generated number:", number)

    attempts += 1

    if number == 8:
        print("Number 8 was found.")
        print("Attempts:", attempts)
        break
