from atm import ATM

if __name__ == "__main__":
    atm = ATM()

    print('======Insert Card======')
    while True:
        card_number = input('xxxx-xxxx-xxxx-xxxx:')
        if not atm.insert_card(card_number):
            print('{} is not valid card number.\n'.format(card_number)) 
            continue
        else:
            break
    print('')

    print('======Insert Pin======')
    while True:
        pin = input('xxxx:')
        if atm.enter_pin(pin): 
            break
        else:
            print('{} is not valid pin.\n'.format(pin))
    print('')

    
    print('======Show Accounts======')
    accounts = atm.show_accounts()
    for account in accounts:
        print('account_number:{}'.format(account))
    print('')


    print('======Select Account======')
    while True:
        account_number = input('xxxx-xxxx:')
        if atm.select_account(account_number):
            break
        else:
            print('{} is not valid account number.\n'.format(account_number))
    print('')


    print('======Transaction======')
    while True:
        action = input("Enter action(balance or deposit or withdraw) or exit:")
        result = None

        if action in ['deposit', 'withdraw']:
            money = int(input('money:'))
            result = atm.transaction(action, money)
        elif action == 'balance':
            result = atm.transaction(action)
        elif action == 'exit':
            break
        else:
            print('{} is not valid action.\n'.format(action))
            continue
        
        print('')
        print('======Result=======')
        print('transaction:', result['status'])
        print('current balance:', result['balance'])
        if result['msg']: print('error msg -', result['msg'])
        print('')

    print('')



        


