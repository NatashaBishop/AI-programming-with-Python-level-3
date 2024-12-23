import numpy as np
# Activation function (ReLU). relu takes negatives and turns them into zeros
def relu(x):
    return np.maximum(0, x)
#Derivative of Sigmoid
def sigmoid(x):
    return  1/(1 + np.exp(-x))
# Define network architecture
input_size = 3
hidden_layer_size = 3
output_size = 2
np.random.seed(42) #generate the same data every time as random value

# Initialize input_data, weights and biases
input_data = np.random.rand(3,1).T

weights = [
    np.random.randn(input_size, hidden_layer_size),
    np.random.randn(hidden_layer_size, output_size)
]
biases = [
    np.random.randn(hidden_layer_size),
    np.random.randn(output_size)
]

# Feedforward function
def feedforwards(inputs, weights, biases):
    layer1_output = relu(np.add(np.dot(input_data, weights[0]), biases[0]))
    layer2_output = sigmoid(np.add(np.dot(layer1_output, weights[1]), biases[1]))
    return layer2_output

FNN= feedforwards(input_data, weights, biases)
print(f'The predicted value is {FNN}')

