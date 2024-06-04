class BankAccount:
    def __init__(self, owner, balance=0):
        """
        Initializes the BankAccount object with an owner and an optional balance (default is 0).
        """
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """
        Deposits the specified amount into the account.
        """
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the account if sufficient balance is available.
        """
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        """
        Returns the current balance of the account.
        """
        return self.balance

# Example usage
account = BankAccount("John Doe", 1000)
account.deposit(500)
account.withdraw(200)
print(f"Final balance: ${account.get_balance()}")
