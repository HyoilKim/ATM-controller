from bank import Bank
from exceptions import AuthException, ActionException

# Insert Card 
# => PIN number 
# => Select Account
# => See Balance/Deposit/Withdraw

class ATM:
    def __init__(self):
        self.bank = Bank()
        self.cashbin = 10000 # 10,000
        self.current_card = None
        self.current_account = None
        self.authuser = False
        self.actions = ['withdraw','deposit','balance']

    def remove_card(self):
        self.current_card = None
        self.current_account = None
        self.authuser = False
    
    def validate_card(self, card_number):
        if self.bank.validate_card(card_number):
            self.current_card = card_number
            return True
        else:
            self.remove_card()
            return False

    def validate_pin(self, pin):
        if self.bank.validate_pin(self.current_card, pin):
            self.authuser = True
            return True
        else:
            self.authuser = False
            return False

    def validate_account(self, account_number):
        if self.bank.validate_account(self.current_card, account_number):
            return True
        else:
            return False

    def show_accounts(self):
        if self.authuser:
            return self.bank.get_accounts(self.current_card)
        else:
            raise AuthException

    def set_account(self, account_number):
        if self.authuser:
            self.current_account = account_number
        else:
            raise AuthException

    def transaction(self, action, money=None):
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
                    self.cashbin -= money
            elif params['action'] == 'deposit':
                params = self.bank.transaction(params)
                self.cashbin += money
            elif params['action'] == 'balance':
                params = self.bank.transaction(params)
        else:
            raise ActionException

        return params
    