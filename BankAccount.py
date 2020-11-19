class BankAccount:
    def __init__(self, full_name, account_number):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = 123456789
        self.balance = 0

account = BankAccount("Laura Apple", )

random_account = list(range(10000000,100000000))