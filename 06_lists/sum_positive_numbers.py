# Sum only positive numbers in a list

total = 0

numbers = [1, 3, 54, 56, 3, -4, 6, 3, -2, 6]

for number in numbers:
    if number < 0:
        continue

    print(number, end=", ")
    total += number

print()
print("Total =", total)
