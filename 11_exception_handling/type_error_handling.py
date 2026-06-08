# Handle TypeError using try-except

try:
    number = 5000
    text = "6000"

    print(number + text)

except Exception as error:
    print("An error occurred.")
    print("Error message:", error)

    if str(error) == "unsupported operand type(s) for +: 'int' and 'str'":
        print("A string and an integer cannot be added together.")
