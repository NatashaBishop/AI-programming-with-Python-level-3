#creating 2 vectors:
import numpy as np 

lst1 = [10,20,30,40,50] #creating lists
lst2 = [1,2,3,4,5]
vctr1 = np.array(lst1) #converting lists into vectors
vctr2= np.array(lst2)
#Addition
vctr_add = vctr1+vctr2
print("Addition of two vectors: ",vctr_add)
#Subtraction
vctr_sub = vctr1-vctr2
print("Subtraction of two vectors: ",vctr_sub)
#Multiplication
vctr_mul = vctr1*vctr2
print("Multiplication of two vectors: ",vctr_mul)
#Division
vctr_div = vctr1/vctr2
print("Division of two vectors: ",vctr_div)

#outut
#Output: 
#Addition of two vectors:  [11 22 33 44 55]
#Subtraction of two vectors:  [ 9 18 27 36 45]
#Multiplication of two vectors:  [ 10  40  90 160 250]
#Division of two vectors: [ 10  10  10 10 10]

