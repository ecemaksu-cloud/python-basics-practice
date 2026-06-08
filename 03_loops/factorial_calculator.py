# Calculate the factorial of a user-entered number

number = int(input("Enter a number: "))

factorial = 1

for i in range(1, number + 1):
    factorial *= i

print("Factorial =", factorial)
