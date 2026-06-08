# Phonebook application with file handling

import ast


class Contact:
    def __init__(self, first_name, last_name, phone="......"):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

    def __str__(self):
        return f"Saved contact: {self.first_name} {self.last_name} {self.phone}"


def show_menu():
    print("**********************")
    print("* Phonebook Program  *")
    print("**********************")
    print("* 1 - Add contact    *")
    print("* 2 - List contacts  *")
    print("* 3 - Search contact *")
    print("* 4 - Exit           *")
    print("**********************")


def add_contact():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    phone = input("Phone number: ")

    contact = {
        "first_name": first_name,
        "last_name": last_name,
        "phone": phone
    }

    with open("phonebook.txt", "a") as file:
        file.write(str(contact) + "\n")

    print("Contact added successfully.")


def list_contacts():
    try:
        with open("phonebook.txt", "r") as file:
            print("Phonebook contact list")
            print("**********************")

            for line in file.readlines():
                contact = ast.literal_eval(line)
                print(contact)

    except FileNotFoundError:
        print("Phonebook file not found.")


def search_contacts():
    try:
        search_name = input("Enter name to search: ").lower()

        with open("phonebook.txt", "r") as file:
            found = False

            for line in file.readlines():
                contact = ast.literal_eval(line)

                if contact["first_name"].lower() == search_name:
                    print("Contact found:", contact)
                    found = True

            if not found:
                print("Contact not found.")

    except FileNotFoundError:
        print("Phonebook file not found.")


while True:
    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        list_contacts()
    elif choice == "3":
        search_contacts()
    elif choice == "4":
        print("Program ended.")
        break
    else:
        print("Invalid choice. Please try again.")
