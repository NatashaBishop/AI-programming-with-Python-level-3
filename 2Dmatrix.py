# matrix is list of lists
# 

# create 2 matrix with 5 interger each
#iterate through and print out one of the matrix using for loop
#vectorized: print(np.matrix(A))

martix_X = [[3,4,5,6,7],[5,6,7,8,9],[7,7,8,10,11],[9,6,3,77,12],[11,23,0,4,0]]
martix_Y = [[4],[6],[8],[10],[12]]
result = []

#for i in range(len(martix_X)):


#multiply 2 matrix: 
for i in range(len(martix_X)):   
   row = martix_X(i)
   temp = []
   for j in range(len(row)): 
     mult = martix_X[i][j]*martix_Y[i][j]
     temp.append(mult)
     result.append(temp)
