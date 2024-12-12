# cardDeck=[4,11,8,5,13,2,6,10]
# hand=[]
# while sum(hand<=17):
#     hand.append(cardDeck.pop())
# print(hand)
#culculate factorial:
# number = 6
# product = 1
# current = 1
# # while number > 0:
# #     product = product*(number)
# #     number = number-1
# # print(product)
# #use for loop
# for i in range(2,number=+1):
#     product *=i
#     number = number-1
# print(product)  
Start_num = 5 # provide some start number, replace 5 with a number you choose
End_num = 100 # provide some end number that you stop when you hit, replace 100 with a number you choose
Count_by = 2 
# provide some number to count by, replace 2 with a number you choose
# # write a while loop that uses 
# break_num as the ongoing number to check against End_num
Break_num = None # replace None with the appropriate code
while Start_num < End_num-2:
    if Start_num>End_num:
        print('Oops! Looks like your start value is greater than the endvalue. Please try again.')
    else:
        Start_num = Start_num+Count_by
    
print(Start_num)

#Activty: Nearest Square
# Write a while loop that finds the largest square number less than an integer 
# limit and stores it in avariable nearest_square. A square number is the product of an integer multiplied by itself, 
# forexample 36 is a square number because if equals 6*6For example, if limit is 40, your code should set the nearest_square to 36.

Limit = 40 # provide a limit, replace 40 with a number you choose# write your while loop here

num=0
#while square <Limit-Start_num:
while (num+1)**2 <Limit:
    num +=1
nearest_square=num**2
print(nearest_square)
#calculate maximum weight the cargo can take.
manifest = [("bananas", 15), ("mattresses", 34), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("curent weight is {}".format(weight))
    if weight >=100:
        print('breaking loop now')
        break
    else:
        print('adding{} ({})'.format(cargo_name,cargo_weight))
        items.append(cargo_name)
        weight +=cargo_weight
print('\nfinal weight: {}'.format(weight))
print('\nfinal items: {}'.format(items))
