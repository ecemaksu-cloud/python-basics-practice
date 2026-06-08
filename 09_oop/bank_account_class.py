# Simple Bank Account Class

class BankAccount:

    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def display_account_info(self):
        print("Name:", self.name)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("New balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("New balance:", self.balance)


account = BankAccount("Mustafa", 123456, 1000)

account.display_account_info()
account.withdraw(300)
account.deposit(500)
