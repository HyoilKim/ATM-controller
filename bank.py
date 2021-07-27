from account import Account
from exceptions import ActionException

dummy = {
    '1234-0000-1234-0000':{
        'accounts': {
            '1234-0000': Account('1234-0000', 100),
            '1234-0001': Account('1234-0001', 1000),
        },
        'pin': '1234'    
    },
    '5678-0000-5678-0000':{
        'accounts': {
            '5678-0000': Account('5678-0000', 200),
            '5678-0001': Account('5678-0001', 2000),
        },
        'pin': '5678'    
    }
}

class Bank:
    def __init__(self):
        self.card_db = dummy

    def validate_pin(self, card_number, pin):
        if self.card_db[card_number]['pin'] == pin:
            return True
        else:
            return False

    def validate_card(self, card_number):
        return card_number in self.card_db

    def validate_account(self, card_number, account_number):
        return account_number in self.card_db[card_number]['accounts']

    def get_accounts(self, card_number):
        return self.card_db[card_number]['accounts']

    def transaction(self, params):
        card_number = params['card_number']
        account_number = params['account_number']
        money = params['money']
        account = self.card_db[card_number]['accounts'][account_number]

        if params['action'] == 'balance':
            params['status'] = 'ok'
        elif params['action'] == 'deposit':
            params['status'] = 'ok'
            account.deposit(money)
        elif params['action'] == 'withdraw':
            if account.withdraw(money):
                params['status'] = 'ok'
            else:
                params['status'] = 'error'
                params['msg'] = 'Not enough balance'
        else:
            raise ActionException

        params['balance'] = account.get_balance()
        return params