# Calculate the average of entered numbers

total = 0
count = 0

number = int(input("Enter a number (0 to exit): "))

while number != 0:
    total += number
    count += 1
    number = int(input("Enter a number (0 to exit): "))

if count > 0:
    average = total / count
    print("Average =", average)
else:
    print("No numbers were entered.")
