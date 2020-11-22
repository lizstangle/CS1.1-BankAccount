class BankAccount():
    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Amount Deposited: ${amount}")
        print(f"Your updated balance amount is: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:

            self.balance -= amount
            print(f"Amount Withdrawn: ${amount}")

        else:
            self.balance -= 10
            return f"Insufficient funds. You have incurred an overdraft fee of $10. Your balance is {self.balance}."
    
    def add_interest(self)
        interest = self.balance * .00083
        self.balance += interest
        return f"Interest has been added, your updated balance is ${self.balance}"

