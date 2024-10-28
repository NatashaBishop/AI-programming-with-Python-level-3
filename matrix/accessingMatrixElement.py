#Two dimensional array is  an array of arrays
#data elements in two dimesnional arrays can be accessed using two indices. 
#One index referring to the main or parent array and another index referring to the position of the data element in the inner array
#If we use only one index then the entire inner array is printed for that index position

from array import * #import the array module, we can directly create an array like this: arr = array('i', [1, 2, 3, 4]) -Creates an array of integers
T = [[11, 12, 5, 2], [15, 6,10,14], [10, 8, 12, 5], [12,15,8,6]]
print(T[0]) #the whole 1st row
print(T[1][2])
#output
#[11, 12, 5, 2]
#10
