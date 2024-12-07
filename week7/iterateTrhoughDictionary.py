#iterate and count number of fruits and culculet them:
result=0
basket_items = {'apples' : 4, 'oranges' : 19, 'kites' : 3, 'sandwiches' : 8}
fruits = ['apples','oranges','pears','peaches','grapes','bananas']

for i in basket_items:
        if i in fruits:
            result=result+basket_items.get(i)
print(result)

#V.2 unfinished: count fruits and the rest separately:
resultFruits=0
resultNonFruits=0
basket_items = {'apples' : 4, 'oranges' : 19, 'kites' : 3, 'sandwiches' : 8}
fruits = ['apples','oranges','pears','peaches','grapes','bananas']

for i in basket_items:
        if i in fruits:
            resultFruits=resultFruits+basket_items.get(i)
        elif:
            resultNonFruits=resultNonFruits+basket_items.get(i)
print(f"Fruits in basket: "+{resultFruits})
print(f"Not fruits in basket: "+{resultNonFruits})
#all items?
