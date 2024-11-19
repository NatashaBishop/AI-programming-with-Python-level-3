#answer format: “ This week’s total sales: xxx” . 
# #you need to take care of the spaces to get the correct answer. 
# Don’t forget  to include a space after the colon “: “.
# in this scenario the data could have been taken from a user input, which is passed as a string as a defoult

Mon_sales = '121'
Tues_sales = '105'
Wed_sales = '110'
Thurs_sales = '98'
Fri_sales = '95'

print(f' This week\'s total sales: {int(Mon_sales)+int(Tues_sales)+int(Wed_sales)+int(Thurs_sales)+int(Fri_sales)} ')

#int(Mon_sales) - we need 2 cast strings in2 interges to perform addition
