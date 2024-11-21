
phone_balance=int(input('what\'s your phone balance?'))
print(type(phone_balance))


if phone_balance<5:

    print('your phone balance is {}. You need phone balance to be more than 5'.format(phone_balance))
else:
    print('your phone balance is {}. You are OK'.format(phone_balance))
