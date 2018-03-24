'''
Activation Function allows models to captuer Non-linearty.
Means it can ideantify the patterns using the curve line

For neural network to achieve the maximum predictive power
we Multiple - Activation Function to the hidden layer.

ReLU - Rectified Linear Activation '''


import numpy as np

input_data = np.array([-1,2])

weights = {'node_0': np.array([3,3]), 'node_1': np.array([1,5]),
           'output': np.array([2,-1])}

node_0_input = (input_data * weights['node_0']).sum()

node_0_output = np.tanh(node_0_input)
# We have use "tanh" activation function here

node_1_input = (input_data * weights['node_1']).sum()

node_1_output = np.tanh(node_1_input)

hidden_layer_output = np.array([node_0_output, node_1_output])

output = (hidden_layer_output * weights['output']).sum()

print(output)

