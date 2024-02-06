class Account:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} accepted. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} accepted. New balance: {self.balance}")
        else:
            print("Insufficient funds. Withdrawal not allowed.")

# Example usage:
account1 = Account("John Doe", 1000)

account1.deposit(500)
account1.withdraw(200)

account1.deposit(1000)
account1.withdraw(1500)  # This should print "Insufficient funds. Withdrawal not allowed."