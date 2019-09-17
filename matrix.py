# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 17:55:31 2019

@author: Ohad
"""
"""
name: Ohad Omrad
class: YB 4
"""
import numpy as np


def Add_UnionAndIdentical_MatrixParts(m1,m2):
    """
    input: two matrix
    output: print the small matrix that sum the unions parts
            and print the big matrix that sum the two matrix
    """
    
    m1Row = np.size(m1,0)  # the number of rows in m1
    m1Col = np.size(m1,1)  # the numbers of colums in m1
    
    # small matrix sizes
    m2Row = np.size(m2,0)  # the number of rows in m2
    m2Col = np.size(m2,1)  # the numbers of colums in m2
    
    #big matrix sizes
    rowmin = min(m1Row, m2Row)  # the common number of rows
    colmin = min(m1Col, m2Col)  # the common number of colums
    
    rowmax = max(m1Row, m2Row)  # the maximum number of rows
    colmax = max(m1Col, m2Col)  # the maximum number of colums
    
    # delte the ununion parts of the two matrix
    newm1 = np.delete(m1, np.s_[rowmin : m1Row], axis=0)
    newm1 = np.delete(newm1, np.s_[colmin : m1Col], axis=1)

    newm2 = np.delete(m2, np.s_[rowmin : m2Row], axis=0)    
    newm2 = np.delete(newm2, np.s_[colmin : m2Col], axis=1)
    
    unionMatrix = np.add(newm1 , newm2)  # this matrix sum the union parts 
                                         #of the two matrix 
    
    print("-- Adding -- union matrix")
    print("")
    print(unionMatrix) 
    
    identicalMatrix = np.zeros((rowmax,colmax))  #creat the big matrix
    #slicing the big matrix in order to sum the two matrix in it
    identicalMatrix[0:m1Row, 0:m1Col] += m1                                          
    identicalMatrix[0:m2Row , 0:m2Col] += m2
    
    print("")
    print("-- Adding -- identical matrix")
    print("")
    print(identicalMatrix)
    
    
def main():
    m1 = np.array([[1, 2,3], [2,3, 4],[4,5,6]])
    m2 = np.array([[2,2],[2,2],[2,2],[4,4]])
    
    print("matrix 1: ")
    print(m1)
    print("matrix 2")
    print(m2)
    print("****************************")
    
    Add_UnionAndIdentical_MatrixParts(m1,m2)

    
if __name__ == "__main__":
    main()