from datetime import datetime
def main():
    balance = 10000
    #repeat=('Y')

    checking_bal=5000
    def __init__(self):
        print('WELCOME')
    class Accountinfo():
       def saving_balance(self):
            print("Your account balance is:",balance)

    now = datetime.now()
    print("Time-Date", now)

    print("XYZ Bank ATM(1234)")
    print('-------------------')
    while True:
        user_pin1 = input('Please enter your PIN: ')
        if len(user_pin1) != 4:
            print('PIN is a 4 digit number')
        else:
            user_pin1 = int(user_pin1)
            break
    while True:
        user_pin2 = input('Please enter your PIN again: ')
        if user_pin1 == user_pin2:
            print('PIN is a 4 digit number')
        else:
            user_pin2 = int(user_pin2)
            break
    if user_pin2 == 1234:

        print("""      WELCOME
 -Choose an option-""")
        print('1. View Balance \n'
              '2. Deposit Amount \n'
              '3. Withdraw Amount \n'
              '4. Transfer funds from checking balance to savings balance \n')
        x = input(" ENTER OPTION NUMBER: ")

        if x == "1":
            user1_balance = Accountinfo()
            user1_balance.saving_balance()
            repeat = input('Would You you like to go back?(Y/N) ')
            if repeat in ('Yes', 'Y', 'y', 'yes'):
                main()
            else:
                print("Thank you for banking with XYZ Bank")
                exit()

        if x == "2":
            deposit = int(input("Enter amount to deposit:  "))

            balance = deposit+balance
            print(deposit,"deposited, Your Current Balance is: ", balance)
            repeat = input('Would You you like to go back?(Y/N) ')
            if repeat in ('Yes', 'Y', 'y', 'yes'):
             main()
            else:
                print("Thank you for banking with XYZ Bank")
                exit()
        if x == "3":
            print("Savings Account Balance:", balance)
            withdraw = int(input("Enter amount to withdraw as 10/50/100/500/1000:  "))

            if withdraw in [10, 50, 100, 500, 1000]:
                balance = balance - withdraw
                print("Collect your money!, Current balance is: ", balance)
                repeat = input('Do you want to continue? (Y/N) ')
                if repeat in ('n', 'NO', 'no', 'N'):
                    print('Thank you for banking with XYZ Bank')
                    exit()
            elif withdraw != [10, 50, 100, 500, 1000]:
                print('Invalid, Please Re-try\n')
                main()


        if x == "4":
            print("Savings Balance:", balance, "Checking Balance:", checking_bal)
            transfer_amt = int(input("Enter amount to transfer:  "))

            if transfer_amt>checking_bal:
                print("The entered amount is larger than your Checking Balance! Try again")
                main()
            else:
                checking_bal = checking_bal - transfer_amt
                balance = balance + transfer_amt
                print(transfer_amt, "Debited from credit balance, Checking Balance is now: ", checking_bal)
                print(transfer_amt, "Transferred to current balance, Current Balance is now: ", balance)
                repeat = input('Would You you like to go back?(Y/N) ')
                if repeat in ('Yes', 'Y', 'y', 'yes'):
                    main()
                else:
                    print("Thank you for banking with XYZ Bank")
                    exit()
        else:
            print("Invalid! , Try Again")
            main()
    else:
            print("Invalid! , Try Again")
            main()
main()



