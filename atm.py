from bank import Bank
from exceptions import AuthException, NotAllowedActionException

# Insert Card 
# => PIN number 
# => Select Account
# => See Balance/Deposit/Withdraw

class ATM:
    def __init__(self):
        self.bank = Bank()
        self.cashbin = 100000 # 100,000
        self.current_card = None
        self.current_account = None
        self.authuser = False
        self.actions = ['withdraw','deposit','balance']

    def remove_card(self) -> None:
        self.current_card = None
        self.current_account = None
        self.authuser = False
    
    def insert_card(self, card_number: str) -> bool:
        if self.bank.validate_card(card_number):
            self.current_card = card_number
            return True
        else:
            self.remove_card()
            return False

    def enter_pin(self, pin: str) -> bool:
        if self.bank.validate_pin(self.current_card, pin):
            self.authuser = True
            return True
        else:
            self.authuser = False
            return False

    def show_accounts(self) -> dict:
        if self.authuser:
            return self.bank.get_accounts(self.current_card)
        else:
            raise AuthException

    def select_account(self, account_number: str) -> bool:
        if self.authuser:
            if self.bank.validate_account(self.current_card, account_number):
                self.current_account = account_number
                return True
            else:
                return False
        else:
            raise AuthException

    def transaction(self, action: str, money=None) -> dict:
        params = {
            'action': action,
            'card_number': self.current_card,
            'account_number': self.current_account,
            'money': money,
            'balance': None,
            'status': None,
            'msg': '',
        }
        
        if params['action'] in self.actions: 
            if params['action'] == 'withdraw':
                if self.cashbin < money:
                    params['status'] = 'error'
                    params['msg'] = 'Not enough cashbin. Current cashbin: {}'.format(self.cashbin)
                else:
                    params = self.bank.transaction(params)
                    if params['status'] == 'ok':
                        self.cashbin -= money
            elif params['action'] == 'deposit':
                params = self.bank.transaction(params)
                if params['status'] == 'ok':
                    self.cashbin += money
            elif params['action'] == 'balance':
                params = self.bank.transaction(params)
        else:
            raise NotAllowedActionException

        return params
    