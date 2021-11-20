# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 09:33:33 2021

@author: Nanto RALIBERA
"""

import numpy as np
from tqdm import tqdm

def build_matrix(matrix_line):
    matrix_line= [x.replace('\n','' ) for x in matrix_line] 
    matrix = np.array([[int(i) for i in x] for x in matrix_line])
    matrix= np.reshape(matrix,(55,108,1))
    return matrix

def build_data (filename):
    matrix_file= open(filename,"r")
    matrix_lines = matrix_file.readlines()
    matrix_file.close()
    
    matrix_lines = [line.replace("\n","") for line in matrix_lines]
    
    
    #initialisation
    list_fault=[matrix_lines[0]]
    matrix_data = build_matrix(matrix_lines[1:56])
    label_data = np.array([0])
    
    for i in tqdm(range(56,len(matrix_lines),56)):
        label_data = np.concatenate([label_data,np.array([i//56])])
        list_fault.append(matrix_lines[i])
        
        matrix=build_matrix(matrix_lines[i+1:i+56])
        matrix_data=np.concatenate([matrix_data,matrix],axis=2)
    
    return matrix_data,label_data,list_fault
        
    
matrix_data,label,list_fault = build_data("fault_matrix_file.txt")


"""print(len(list_fault))
print(label)
print(np.shape(matrix_data))"""

