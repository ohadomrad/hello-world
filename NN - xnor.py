# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 16:27:45 2019

@author: Ohad
"""
"""
notess:
    - Name: Ohad Omrad
    - class:YB 4
    
    - this system is Neural Network that learn to calculate x1 xnor x2 xnor x3
    
    - the learning data:
        
            * * * * * * * * * * * * 
            * 1 xnor 1 xnor 1 = 1 *
            * 1 xnor 0 xnor 0 = 1 *
            * 1 xnor 0 xnor 1 = 0 *
            * 0 xnor 0 xnor 1 = 1 *
            * 0 xnor 1 xnor 1 = 0 *
            * 0 xnor 1 xnor 0 = 1 *
            * * * * * * * * * * * *
            
    - the missing data:
            * * * * * * * * * * * * 
            * 1 xnor 1 xnor 0 = 0 *
            * 0 xnor 0 xnor 0 = 0 *
            * * * * * * * * * * * *
            
    - I implement this NN using a class that contains:
        * The attributes: bias , list of weights
        * The method: 
                       __init__(self, bias) - constractor
                       sigmoind(self, x) - activation function
                       sigmoid_derivative(self, x)
                       train_inputs(self, inputs, output) - train one exercise
                       get_result(self, inputs) - return the NN output
                       get_x(self, inputs) - return the value that the 
                                             activation function get
    
    - I implement a function that get a NN object and train the current nn
       with 6 of the options (their is 8: 2^3) x1 xnor x2 xnor x3:
           train(neural_net, nun_iterations) - the train function
     
    - In main function i created an NN object, train its and call to get_result
      with the user inputs
"""

import numpy as np
# all the possible inputs options
allOptions = np.array([[1,1,1], [1,1,0], [1,0,1], [1,0,0], [0,1,1], [0,1,0],[0,0,1], [0,0,0]])

class NN:
    
    def __init__(self, bias, lr):
        """
        input: the bias, lr - learning rate
        output: NN object
        """
        self.bias = bias #value of bias
        self.lr = lr
       
        np.random.seed(1)
        
        self.weights = 2 * np.random.random((4, 1)) - 1
        print(self.weights)
    
    def sigmoid(self, x):
        """
        Action Function
        input: x value
        output: sigmoind(x) value
        """
        return 1 / (1 + np.exp(-x))
    
    
    def sigmoid_derivative(self, x):
        """
        Action Function
        input: sigmoind(x) value
        output: sigmoid_derivative(sigmoind(x)) = sigmoind(x) * (1-sigmoind(x))
        """
        return x * (1 - x)
    
    
    def train_inputs(self, inputs, output):
        """
        input: list of the binari inputs, the correct output for this inputs
        
        this function change the inputs's weight in order to get more exact
        output
        
        this function will be called a lot of times in order to train
        the Neural Network
        """
        train_output = self.sigmoid(self.get_X(inputs))
        error = output - train_output
        for i in range(3):
            self.weights[i] += (inputs[i] * error * self.lr *
                              self.sigmoid_derivative(train_output))
        
        self.weights[3] += (self.bias * error * self.lr *
                            self.sigmoid_derivative(train_output))
        

    def get_X(self, inputs):
        
        """
        input: the 3 binari inputs
        output: the value that the actiovation function get
        """
        x = 0
        inputs = inputs.astype(float)
        for i in range(3):
            x += (inputs[i] * self.weights[i])
        
        x += self.bias *  self.weights[3]
        
        return x
        
    
    def get_result(self, inputs):
        """
        input: the list of the binari inputs
        output: the output fot this inputs of the Neural Network
        """
        
        output = self.sigmoid(self.get_X(inputs))
        
        if output > 0.5:
            output = 1
        else:
            output = 0
        
        return output
        
        
def train(neural_net, nun_iterations):
    """
    input: a NN object (nun_iterations), num of iterations
                                        (how many tines to train the NN)
    
    this function called to the NN's train method
    in order to train the NN system                                
    """
    print('\n-- Train --\n')
    
    print('---> Num Iterations: ' , nun_iterations)
    print('----> the trained data: \n')
    print('1 xnor 1 xnor 1 = 1')
    print('1 xnor 0 xnor 0 = 1')
    print('1 xnor 0 xnor 1 = 0')
    print('0 xnor 0 xnor 1 = 1')
    print('0 xnor 1 xnor 1 = 0')
    print('0 xnor 1 xnor 0 = 1\n\n')
    
    for i in range(nun_iterations):
        neural_net.train_inputs(np.array([1,1,1]), 1)
        neural_net.train_inputs(np.array([1,0,0]), 1)
        neural_net.train_inputs(np.array([1,0,1]), 0)
        neural_net.train_inputs(np.array([0,0,1]), 1)
        neural_net.train_inputs(np.array([0,1,1]), 0)
        neural_net.train_inputs(np.array([0,1,0]), 1)
    
    
def get_inputs():
    """
    absorb binary inputs from the user and return them in a list
    """
    inputs = np.array([float(input('Enter binary input 1: ')),
                      float(input('Enter binary input 2: ')),
                      float(input('Enter binary input 3: '))])
    return inputs

    
def prints(neural_net, inputs):
    """
    inputs: the neural_net and the inputs
    output: prints the output for this inputs
    """
    res = neural_net.get_result(inputs)
    print(inputs[0], " xnor ", inputs[1], " xnor", inputs[2] , " = ", res)   
    
   
def cheak(neural_net):
    """
    input: the neural_net
    output: all the existsting exercise and their outputs
    """
    for i in range(8):
        prints(neural_net, allOptions[i])
        
def main():
    
    neural_net = NN(0,1)
    train(neural_net, 5000)

    prints(neural_net, get_inputs())
    #cheak(neural_net)
    
if __name__ == '__main__':
    main()