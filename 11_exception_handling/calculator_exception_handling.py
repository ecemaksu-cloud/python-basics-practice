# Calculator with exception handling

try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))

    operation = input("Operation (+, -, *, /): ")

    if operation == "+":
        print(number1 + number2)

    elif operation == "-":
        print(number1 - number2)

    elif operation == "*":
        print(number1 * number2)

    elif operation == "/":
        print(number1 / number2)

except ZeroDivisionError as error:
    print(f"Division by zero is not allowed. Error: {error}")

except ValueError as error:
    print(f"Invalid input. Please enter numbers only. Error: {error}")

except Exception as error:
    print(f"Unexpected error occurred: {error}")
