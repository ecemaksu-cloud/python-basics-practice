# Custom exception example for user registration

class CustomError(Exception):

    def __init__(self, message="An error occurred"):
        self.message = message
        super().__init__(f"Warning! {message}")


print("LOGIN SCREEN")

try:
    print("Create a new user")

    national_id = input("National ID: ")
    password = input("Password: ")

    if len(password) < 4:
        raise CustomError("Password must contain at least 4 characters.")

    if len(national_id) > 11:
        raise CustomError("National ID cannot be longer than 11 digits.")

    print("User created successfully.")

except CustomError as error:
    print("Input validation error:")
    print(error)
