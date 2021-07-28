from atm import ATM
from bank import Bank
from exceptions import AuthException, NotAllowedActionException
import unittest

class ATMControllerTest(unittest.TestCase):
    def test_atm(self):
        atm = ATM()
        self.assertEqual(atm.cashbin, 100000)

    def test_card(self):
        atm = ATM()

        # valid card
        result = atm.insert_card('1234-0000-1234-0000')
        self.assertEqual(result, True)
        self.assertEqual(atm.current_card, '1234-0000-1234-0000')
        
        # remove card
        atm.remove_card()
        self.assertEqual(atm.current_card, None)

        # invalid card
        result = atm.insert_card('0000-0000-0000-0000')
        self.assertEqual(result, False)
        self.assertEqual(atm.current_card, None)


    def test_pin(self):
        atm = ATM()
        
        # valid pin
        atm.insert_card('1234-0000-1234-0000')
        atm.enter_pin('1234')
        self.assertEqual(atm.authuser, True)

        # remove card
        atm.remove_card()
        self.assertEqual(atm.current_card, None)
        self.assertEqual(atm.authuser, False)

        # invalid pin
        atm.insert_card('1234-0000-1234-0000')
        atm.enter_pin('0000')
        self.assertEqual(atm.authuser, False)

    def test_accounts(self):
        atm = ATM()
        bank = Bank()

        # valid account
        atm.insert_card('1234-0000-1234-0000')
        atm.enter_pin('1234')
        atm.select_account('1234-0000')
        self.assertEqual(atm.current_account, '1234-0000')

        # remove card
        atm.remove_card()
        self.assertEqual(atm.current_card, None)
        self.assertEqual(atm.authuser, False)
        self.assertEqual(atm.current_account, None)

        # invalid account
        atm.insert_card('1234-0000-1234-0000')
        atm.enter_pin('1234')
        result = atm.select_account('1234-1234')
        self.assertEqual(result, False)
        self.assertEqual(atm.current_account, None)

    def test_transactions(self):
        atm = ATM()
        bank = Bank()

        # init
        atm.insert_card('1234-0000-1234-0000')
        atm.enter_pin('1234')
        atm.select_account('1234-0000')

        # valid trasaction(balance)
        result = atm.transaction('balance')
        self.assertEqual(result['action'], 'balance')
        self.assertEqual(result['card_number'], '1234-0000-1234-0000')
        self.assertEqual(result['account_number'], '1234-0000')
        self.assertEqual(result['money'], None)
        self.assertEqual(result['balance'], 100)
        self.assertEqual(result['status'], 'ok')
        self.assertEqual(result['msg'], '')

        # valid trasaction(deposit)
        result = atm.transaction('deposit', 10)
        self.assertEqual(result['action'], 'deposit')
        self.assertEqual(result['card_number'], '1234-0000-1234-0000')
        self.assertEqual(result['account_number'], '1234-0000')
        self.assertEqual(result['money'], 10)
        self.assertEqual(result['balance'], 110)
        self.assertEqual(result['status'], 'ok')
        self.assertEqual(result['msg'], '')
        self.assertEqual(atm.cashbin, 100010)
        
        # valid trasaction(withdraw)
        result = atm.transaction('withdraw', 10)
        self.assertEqual(result['action'], 'withdraw')
        self.assertEqual(result['card_number'], '1234-0000-1234-0000')
        self.assertEqual(result['account_number'], '1234-0000')
        self.assertEqual(result['money'], 10)
        self.assertEqual(result['balance'], 100)
        self.assertEqual(result['status'], 'ok')
        self.assertEqual(result['msg'], '')
        self.assertEqual(atm.cashbin, 100000)

        # invalid transaction(deposit, )
        result = atm.transaction('deposit')
        self.assertEqual(result['action'], 'deposit')
        self.assertEqual(result['card_number'], '1234-0000-1234-0000')
        self.assertEqual(result['account_number'], '1234-0000')
        self.assertEqual(result['money'], None)
        self.assertEqual(result['balance'], 100)
        self.assertEqual(result['status'], 'error')
        self.assertEqual(result['msg'], 'No input money')

        # invalid trasaction(withdraw, not enough balance)
        result = atm.transaction('withdraw', 1000)
        self.assertEqual(result['action'], 'withdraw')
        self.assertEqual(result['card_number'], '1234-0000-1234-0000')
        self.assertEqual(result['account_number'], '1234-0000')
        self.assertEqual(result['money'], 1000)
        self.assertEqual(result['balance'], 100)
        self.assertEqual(result['status'], 'error')
        self.assertEqual(result['msg'], 'Not enough balance')
        self.assertEqual(atm.cashbin, 100000) 

        # invalid trasaction(withdraw, not enough cashbin)
        atm.cashbin = 0
        result = atm.transaction('withdraw', 10)
        self.assertEqual(result['action'], 'withdraw')
        self.assertEqual(result['card_number'], '1234-0000-1234-0000')
        self.assertEqual(result['account_number'], '1234-0000')
        self.assertEqual(result['money'], 10)
        self.assertEqual(result['balance'], None) # bank api를 호출하지 않아서 모른다
        self.assertEqual(result['status'], 'error')
        self.assertEqual(result['msg'], 'Not enough cashbin. Current cashbin: 0')
        self.assertEqual(atm.cashbin, 0) 

    def test_auth_exception(self):
        atm = ATM()
        with self.assertRaises(AuthException):
            atm.insert_card('1234-0000-1234-0000')
            atm.enter_pin('1234')
            atm.authuser = False
            atm.select_account('1234-0000')

    def test_action_exception(self):
        atm = ATM()
        with self.assertRaises(NotAllowedActionException):
            atm.insert_card('1234-0000-1234-0000')
            atm.enter_pin('1234')
            atm.select_account('1234-0000')
            atm.transaction('invalid action')

if __name__ == "__main__":
    unittest.main()