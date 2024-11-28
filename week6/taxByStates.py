stateInputed=input('Please, input your state code, please: ').upper()
amoutInputed=int(input('Please, input your purchase amount: '))

                 
if stateInputed=="CA":
    print(f'You tax is 7.5% and the total you have to pay is {amoutInputed+amoutInputed*0.075}')
elif stateInputed=="MN":
    print(f'You tax is 9.5% and the total you have to pay is {amoutInputed+amoutInputed*0.095}')
elif stateInputed=="NY":
    print(f'You tax is 8.9% and the total you have to pay is {amoutInputed+amoutInputed*0.089}')
else:
    print('Input error')
