from account import Account
from exceptions import NotAllowedActionException

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

    def validate_pin(self, card_number: str, pin: str) -> bool:
        if self.card_db[card_number]['pin'] == pin:
            return True
        else:
            return False

    def validate_card(self, card_number: str) -> bool:
        return card_number in self.card_db

    def validate_account(self, card_number: str, account_number: str) -> bool:
        return account_number in self.card_db[card_number]['accounts']

    def get_accounts(self, card_number: str) -> bool:
        return self.card_db[card_number]['accounts']

    def transaction(self, params: dict) -> dict:
        card_number = params['card_number']
        account_number = params['account_number']
        money = params['money']
        account = self.card_db[card_number]['accounts'][account_number]

        if params['action'] == 'balance':
            params['status'] = 'ok'
        elif params['action'] == 'deposit':
            if not money:
                params['status'] = 'error'
                params['msg'] = 'No input money'
            else:
                params['status'] = 'ok'
                account.deposit(money)
        elif params['action'] == 'withdraw':
            if not money:
                params['status'] = 'error'
                params['msg'] = 'No input money'
            else:
                if account.withdraw(money):
                    params['status'] = 'ok'
                else:
                    params['status'] = 'error'
                    params['msg'] = 'Not enough balance'
        else:
            raise NotAllowedActionException

        params['balance'] = account.get_balance()
        return params