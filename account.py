class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, money: int):
        self.balance += money

    def withdraw(self, money: int):
        if money > self.balance:
            return False
        else:
            self.balance -= money  
            return True

    def get_balance(self):
        return self.balance