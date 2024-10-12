#inpired by https://www.digitalocean.com/community/tutorials/vectors-in-python
#vector is a one-dimensional array of lists
#We use numpy.array() method to create a one-dimensional array i.e. a vector
#syntax: Syntax: numpy.array(list)

import numpy as np 
lst = [10,20,30,40,50] 
vctr = np.array(lst) 
print("Vector created from a list:") 
print(vctr) 
#outup
#Vector created from a list:
#[10 20 30 40 50]
