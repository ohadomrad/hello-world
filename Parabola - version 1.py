# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 14:43:25 2019

@author: Ohad
"""
"""
Name: Ohad Omrad

version 1 - the distaces are defined on Y axis
"""

import numpy as np
import matplotlib.pyplot as plt

def getCoefficients():
    """
    input: the function absorb the parabola coefficients (a,b,c)
    parabola = a*x*x + b*x + c
    output: the function return in a list the coefficients [a,b,c]
    """
    print("Please enter the parabula coefficients(a,b,c) a*x^2 + b*x + c" )
    a = int (input("Enter a = "))
    b = int(input("Enter b = "))
    c = int(input("Enter c = "))
    
    return [a,b,c]


def getFunction(a,b,c):
    """
    input: the function get the coefficients (a,b,c)
    output: the function return in a list: [0]  - the function range (x)
                                           [1] - a list of function values f(x)
                                                   
    """
    xrange = np.arange(0,100, 0.1)
    f = [a*x*x + b*x + c for x in xrange]
    return [xrange,f]


def printParabula(a,b,c):
    """
    input: the function get the coefficients (a,b,c)
    output: the function ptints the parabola
        
    """
    print("-- Function --")
    func = getFunction(a,b,c)
    x = func[0]  # function x range
    f = func[1]  # list with the function values
    
    plt.plot(x,f)
    
    plt.xlabel('x axis label')
    plt.ylabel('y axis label')
    
    plt.title('Parabola')
    plt.show()


def getPoints():
    """
    input: the fuction absorb 10 points in a list (list of points)
    output: the function return the point list
    """
    print("-- Get Points --")
    points = []  # the points list
    for i in range(0,10):
        x = int (input("Enter x = "))
        y = int(input("Enter y = "))
        points.append([x,y])
    return points

    
def getSumDistances(points, a,b,c):
    """
    input: the point list, the parabola coefficients (a,b,c)
    output: return a list with: [0] -  sum of the distances between the points
                                       to the function 
                                [1] - the number of points that belong to the
                                      function
    """
    func = getFunction(a,b,c)
    x = func[0]
    f = func[1]
    polinom = np.poly1d(np.polyfit(x, f,2))
    
    dis = 0        # the distance between the point to the function on Y axis
    sumDis = 0     # the sum of the all distances
    counter = 0    # the counter is counting the number of points that on
                   # the parabola
    
    for point in points:
        dis = np.abs(polinom(point[0]) - point[1])
        if dis == 0:
            counter += 1
        else:
            sumDis += dis
    
    return [sumDis, counter]
         
    
def getTheMaxPatabolaAccuracy(points):
    """
    input: get the points list
    output: absorb parabola coefficients (a,b,c) and find the parabola that
            the most closed to the points
    """
    print("\n-- Finding The Match Parabola --\n")
    func = getCoefficients()
    # minSum - the minimum sum distances betweem all the function to the points
    minSum = getSumDistances(points,func[0],func[1],func[2])[0]
    #minFunc - the function that her sum Distances is the minimal
    minFunc = func
    
    for i in range(0,49):
        func = getCoefficients()
        # sumDis - the sum of the distances in the specific parabola
        sumDis = getSumDistances(points,func[0],func[1],func[2])[0]
        
        if(sumDis < minSum):
            minSum = sumDis
            minFunc = func
        
    return minFunc
    

def main():

    p = getCoefficients()
    printParabula(p[0], p[1], p[2])
    points = getPoints()
    
    detailsList = getSumDistances(points, p[0], p[1], p[2])
    print("\n-- Details --\n")
    print("sum distances: " , detailsList[0])
    print("The number of points that belong to the function: ",detailsList[1])
    print("\n***************************************\n")
    print("The parabola that the most closed to the points",
          getTheMaxPatabolaAccuracy(points))
    
    
if __name__ == "__main__":
    main()