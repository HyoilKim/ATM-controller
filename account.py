class Account:
    def __init__(self, account_number: str, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, money: int) -> None:
        self.balance += money

    def withdraw(self, money: int) -> bool:
        if money > self.balance:
            return False
        else:
            self.balance -= money  
            return True

    def get_balance(self) -> int:
        return self.balance