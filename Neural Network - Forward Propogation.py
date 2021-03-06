''' Suppose we have to determing How many transactions a person makes based
on the number of Childrens and the number of Accounts. The following
Neural Network shows the user with 2 childrens and 3 accounts. '''

import numpy as np

input_data = np.array([2,3])     # The input has two values 2 and 3

weights = {'node_0':np.array([1,1]), 'node_1':np.array([-1,1]), 'output': np.array([2,-1])}
#We have define the weights of each input node and output

node_0_value = (input_data * weights['node_0']).sum()

node_1_value = (input_data * weights['node_1']).sum()

hidden_layer_values = np.array([node_0_value, node_1_value])

output = (hidden_layer_values * weights['output']).sum()

print(hidden_layer_values) # It will print the values of the hidden layers

print(output) # Gives the total number of transctions user makes


