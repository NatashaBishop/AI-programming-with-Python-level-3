number2guess=4
numberInputed=int(input('Input your number, please '))
                 
if numberInputed<number2guess:
    print('You number is too low')
elif numberInputed>number2guess:
    print('You number is too high')
else:
    print('You have guessed the number')


