#  Bear Robotics coding assessment 
## ATM-controller
Write code for a simple ATM. It doesn't need any UI (either graphical or console), but a controller should be implemented and tested.

### Assessment requirements
At least the following flow should be implemented:

Insert Card => PIN number => Select Account => See Balance/Deposit/Withdraw

For simplification, there are only 1 dollar bills in this world, no cents. Thus account balance can be represented in integer.

Your code doesn't need to integrate with a real bank system, but keep in mind that we may want to integrate it with a real bank system in the future. It doesn't have to integrate with a real cash bin in the ATM, but keep in mind that we'd want to integrate with that in the future. And even if we integrate it with them, we'd like to test our code. Implementing bank integration and ATM hardware like cash bin and card reader is not a scope of this task, but testing the controller part (not including bank system, cash bin etc) is within the scope.

A bank API wouldn't give the ATM the PIN number, but it can tell you if the PIN number is correct or not.

Based on your work, another engineer should be able to implement the user interface. You don't need to implement any REST API, RPC, network communication etc, but just functions/classes/methods, etc.

You can simplify some complex real world problems if you think it's not worth illustrating in the project.

### Code Description
- class ATM(ATM.py) 
    - variables
      - `bank`: can access bank api
      - `cashbin`: atm having money 
      - `current_card`: having card number or None
      - `current_account`: having account number or None
      - `authuser`: True or False
      - `actions`: transactions(withdraw, deposit, balance)
    - methods
      - `remove_card`: init variables
      - `insert_card`: validate and set card number
      - `enter_pin`: validate pin and set authuser
      - `show_accounts`: show accounts using current card
      - `select_account`: validate and set account
      - `trasaction`: check cashbin and call bank's transaction
      
- class Bank(bank.py)
    - `dummy`: ***db, data in dummy is only valid***
      ```json
        dummy = {
          "1234-0000-1234-0000":{
              "accounts": {
                  "1234-0000": Account("1234-0000", 100),
                  "1234-0001": Account("1234-0001", 1000),
              },
              "pin": "1234" 
          },
          "5678-0000-5678-0000":{
              "accounts": {
                  "5678-0000": Account("5678-0000", 200),
                  "5678-0001": Account("5678-0001", 2000),
              },
              "pin": "5678"
           }
         }
    - variable
        - `card_db`: dummy data
    - methods
        - `validate_pin`: check card_number and pin is correct
        - `validate_card`: check card_number in db
        - `validate_account`: check account in db
        - `get_accounts`: return accounts using card_number
        - `transaction`: execute actions and return result

### How to run

1. Download source code </br>
`git clone https://github.com/kimhyoil/ATM-controller.git`

2. Enter root directory
3. Run code (my python version: 3.9.5)
- `python main.py`
- `python test.py -v`

### Demo
1. Inset Card (Enter card number)
2. PIN number (Enter pin number)
3. Select Account (Select account on screen)
4. See Balance
5. Deposit
6. Withdraw
7. See Balance
8. Exit

![image](https://user-images.githubusercontent.com/23691938/127266199-445d7133-5f22-4857-a30d-549db3d72adf.png)

![image](https://user-images.githubusercontent.com/23691938/127266411-90d4ae60-2ed0-43bd-aa86-6136705f115a.png)
