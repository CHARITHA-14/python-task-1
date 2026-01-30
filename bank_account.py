# Mini Banking System using OOP Concepts
class BankAccount:
    """
    Base class representing a generic bank account
    """

    def __init__(self, account_number, holder_name, balance=0):
        # Attributes
        self.account_number = account_number
        self.holder_name = holder_name
        self.__balance = balance   # Encapsulation (private variable)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("❌ Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("❌ Insufficient balance.")

    def get_balance(self):
        return self.__balance

    def display_details(self):
        print("\n--- Account Details ---")
        print("Account Number:", self.account_number)
        print("Account Holder:", self.holder_name)
        print("Balance: ₹", self.__balance)


# Inheritance
class SavingsAccount(BankAccount):
    """
    Derived class representing a savings account
    """

    def __init__(self, account_number, holder_name, balance=0, interest_rate=0.04):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    # Method overriding
    def add_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print("Interest added successfully.")

    def display_details(self):
        # Overridden method
        super().display_details()
        print("Account Type: Savings")
        print("Interest Rate:", self.interest_rate * 100, "%")


# Main Program (Simulation)
if __name__ == "__main__":

    # Creating multiple objects
    acc1 = BankAccount(101, "Charitha Sri", 5000)
    acc2 = SavingsAccount(102, "Ravi Kumar", 10000)

    # Simulating real bank operations
    acc1.deposit(2000)
    acc1.withdraw(1000)
    acc1.display_details()

    acc2.deposit(3000)
    acc2.add_interest()
    acc2.withdraw(2000)
    acc2.display_details()
