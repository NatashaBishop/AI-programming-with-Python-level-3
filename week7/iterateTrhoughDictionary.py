#iterate and count number of fruits:
result=0
basket_items = {'apples' : 4, 'oranges' : 19, 'kites' : 3, 'sandwiches' : 8}
fruits = ['apples','oranges','pears','peaches','grapes','bananas']

for i in basket_items:
        if i in fruits:
            result=result+basket_items.get(i)
print(result)
