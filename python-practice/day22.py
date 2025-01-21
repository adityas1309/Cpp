# Question: Day 22: Create a BankAccount class with deposit/withdraw methods and balance tracking.
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

# Usage example
account = BankAccount(100)
account.withdraw(50)
account.deposit(200)
