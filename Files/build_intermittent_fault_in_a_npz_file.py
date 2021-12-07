# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 11:22:47 2021

@author: Nanto RALIBERA
"""

import numpy as np
import random as rd
from tqdm import tqdm
from build_data import build_matrix

#LOAD DATA
#building the right_matrix
right_matrix_file=open("right_matrix.txt","r")
right_matrix = build_matrix(right_matrix_file.readlines())
right_matrix_file.close()

#build permanent fault
matrix_data = np.load("permanent_fault_array.npy")
label = np.load("fault_label.npy")


#build intermittent fault
activation_rate = 0.85 #85% des vecteurs de la faute permanente restent intacts le reste est remplacés
nb_of_intermittent_fault=100


for i in tqdm(range(matrix_data.shape[2])): #on fait des fautes intermittentes pour chaque classe de fautes
    filename="intermittent_fault_array"+str(i)
    faulty_line=[]
    
    final_matrix = np.copy(matrix_data[:,:,i])
    final_matrix = np.reshape(final_matrix,(1,55,108))
    
    final_label = np.array([label[i]])
    
    
    matrix_copy= np.copy(matrix_data[:,:,i])
    matrix_copy= np.reshape(matrix_copy,(1,55,108))
    
    
    for j in range(matrix_data.shape[0]): #get the faulty lines
        for k in range(108):
            if  matrix_copy[0,j,k] != right_matrix[j,k,0]:
                faulty_line.append(j)
                break
    

    #change faulty line
    list_of_sample =[]
    for index in range(nb_of_intermittent_fault):
        nb_of_vect_to_change=int((1-activation_rate)*len(faulty_line))
        
        sample = rd.sample(faulty_line,nb_of_vect_to_change)
        
        
        if sample not in list_of_sample:
            list_of_sample.append(sample) 


    for elem1 in list_of_sample:
        for elem2 in range(len(elem1)):
            matrix_copy[0,elem1[elem2],:] = right_matrix[elem1[elem2],:,0]
        final_label=np.concatenate([final_label,np.array([i])])
        final_matrix=np.concatenate([final_matrix,matrix_copy],axis=0)
        
        matrix_copy= np.copy(matrix_data[:,:,i])
        matrix_copy= np.reshape(matrix_copy,(1,55,108))
    
    
    np.savez_compressed(filename,matrix=final_matrix,label=final_label)