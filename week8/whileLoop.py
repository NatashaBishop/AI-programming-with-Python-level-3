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
while Start_num > 5 and End_num<100:
    if Start_num>End_num:
        print('Oops! Looks like your start value is greater than the endvalue. Please try again.')
    else:
        Start_num = Start_num+Count_by
    
print(Start_num)
