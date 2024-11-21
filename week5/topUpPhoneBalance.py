#unfinished
phone_balance=int(input('what\'s your phone balance?'))
bank_balance=int(input('what\'s your phone bank balance?'))
 print(type(phone_balance))


if phone_balance<5:

    print('your phone balance is {}, but you need your bank balance 2 b mohe thqn 10 to pay into phone balance You need phone balance to be more than 5'.format(phone_balance))
else:
    print('your phone balance is {}. You are OK'.format(phone_balance))


if phone_balance<5:
    phone_balance+=10
    bank_balance-=10
print('You new phone balance is: {}'.format(phone_balance))
print('You new bank balance is: {}'.format(bank_balance))
