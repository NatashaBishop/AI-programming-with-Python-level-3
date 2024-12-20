import numpy as np
#in next exersise define the neuro network arcitecture

#in this
#define variables to hold vector data:
#list to hold input layer data
x_var = [1,-0.5,3]
#2d matrix to hold data for waits for hidden layer:
w1_waits = [[1,2,-2],
            [3,-2,2],
            [-1,2,4]]
#list to hold data for waits for output layer:
w2_waits = [-6, 10, 10]

x = np.array(x_var) #converting list data into vector
w1 = np.array(w1_waits) #vectorize waits
w2 = np.array(w2_waits) #vectorize waits
b4_hidden_layer = np.dot(x,w1) #dot product of x and w1
#print(b4_hidden_layer)
#relu is changing negative numbers to zero, getting rid of them
def relu(X):
    return np.maximum(0,X)
hidden_layer_after_relu = relu(b4_hidden_layer) # hERE YOU APPLIED relu on the sum of the products of the input data and the weight from input to the hidden layer

output_b4_relu = np.dot(hidden_layer_after_relu,w2) #after applying relu to hidden layer, we are getting dot product from that result and vectorized waits for output layer

#print(output_b4_relu)
output = relu(output_b4_relu) # applying relu to output layer for final output
print(output)
