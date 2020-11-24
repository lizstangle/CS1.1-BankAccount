import random
class BankAccount:
    def __init__(self, full_name, account_number, routing_number, balance=0):
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
            print(f"Insufficient funds. You have incurred an overdraft fee of $10. Your balance is {self.balance}.")
    
    def get_balance(self):
        print(f"Your balance is {self.balance}")

    def add_interest(self):
        interest = self.balance * .00083
        self.balance += interest
        print(f"Interest has been added, your updated balance is ${self.balance}")

    def receipt(self):
        print("****************")
        print(f"Name: {self.full_name}")
        print(f"Account No.: {self.account_number}")
        print(f"Routing No.: {self.routing_number}")
        print(f"Balance: {self.balance}")
        print("****************")

def AccountNum():
    number = random.randint(10000000, 99999999)
    return number

routing = 123456789

person = BankAccount("Beverly Cleary", AccountNum(), routing, 1000)
person.deposit(100)
person.withdraw(60)
person.get_balance()
person.add_interest()
person.receipt()


person1 = BankAccount("Judy Blume", AccountNum(), 987654321, 2000)
person1.deposit(200)
person1.withdraw(300)
person1.get_balance()
person1.add_interest()
person1.receipt()

person2 = BankAccount("Simone de Beauvoir", AccountNum(), 987654321, 5000)
person2.deposit(1000)
person2.withdraw(6100)
person2.get_balance()
person2.add_interest()
person2.receipt()