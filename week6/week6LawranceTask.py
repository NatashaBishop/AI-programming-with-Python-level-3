#Starter Activity
#You were given the code below .
#Create a Jupyter Notebook python file which:
#Create two 2 dimensional matrices
#Call the dot_product function and pass the created matrices as arguments.

import numpy as np
list_one=[[1,2,3],[4,5,6],[7,8,9]]
list_two=[[11,22,33],[44,55,66],[77,88,99]]
vector_one=np.array(list_one)
vector_two=np.array(list_two)
def dot_product(vector_one, vector_two):
   result= 0
   
   for i in range(len(vector_one)):
    result+= vector_one[i] * vector_two[i]
 
   return result
print(dot_product(vector_one, vector_two))
