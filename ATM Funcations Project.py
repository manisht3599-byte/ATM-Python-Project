from Funcation import *
account_balance=50000.00
account_number='12345678'
pin='1234'
print('Welcome to punjab national bank')
print()
print('1-show account balance')
print('2-cash deposit:')
print('3-cash withdrawal:')
print('4-pin change')
print()
opt=input('Enter the number to proceed:')
if opt=='1':
    user_pin=input('Enter your pin number:')
    show_acc_balance(user_pin,pin,account_balance)
elif opt=='2':
    user_pin=input('Enter your pin number:')
    cash_depost(user_pin,pin,account_balance)
elif opt=='3':
    user_pin=input('Enter your pin number:')
    cash_withdraw(user_pin,pin,account_balance)
elif opt=='4':
    user_pin=input('Enter your pin number:')
    pin_change(user_pin,pin)
else:
    print('please enter a valid option')
