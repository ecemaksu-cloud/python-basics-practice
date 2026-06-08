# Perform basic arithmetic operations using a function

def basic_calculator(num1, num2):
    print("Addition =", num1 + num2)
    print("Subtraction =", num1 - num2)
    print("Multiplication =", num1 * num2)
    print("Division =", num1 / num2)

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

basic_calculator(number1, number2)
