# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 09:33:33 2021

@author: Nanto RALIBERA
"""

import numpy as np

def build_matrix(matrix_line):
    matrix_line= [x.replace('\n','' ) for x in matrix_line] 
    matrix = np.array([[int(i) for i in x] for x in matrix_line])
    matrix= np.reshape(matrix,(55,108,1))
    return matrix



"""matrix=build_matrix(open("right_matrix.txt","r").readlines(),1)
print (np.shape(matrix))
print(matrix)"""