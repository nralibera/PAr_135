# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 11:22:47 2021

@author: Nanto RALIBERA
"""
 
import numpy as np
import random as rd
from tqdm import tqdm
import os


#LOAD DATA
#building the right_matrix

right_matrix=np.load("right_matrix.npy")

#build permanent fault
matrix_data = np.load("permanent_fault_array.npy")
label = np.load("fault_label.npy")


#build intermittent fault
#activation_rate = 0.85 #85% des vecteurs de la faute permanente restent intacts le reste est remplacés
nb_of_intermittent_fault=100
nb_activ_rate=5

    
for i in tqdm(range(matrix_data.shape[2])): #on fait des fautes intermittentes pour chaque classe de fautes
    filename="intermittent_fault_array"+str(i)
    faulty_line=[]
    
    final_matrix = np.copy(matrix_data[:,:,i])
    final_matrix = np.reshape(final_matrix,(55,108))
    
    final_label = np.array([label[i]])
    
    
    matrix_copy= np.copy(matrix_data[:,:,i])
    matrix_copy= np.reshape(matrix_copy,(55,108))
    
    
    for j in range(matrix_data.shape[0]): #get the faulty lines
        for k in range(108):
            if  matrix_copy[j,k] != right_matrix[j,k,0]:
                faulty_line.append(j)
                break
    
    for k in range(nb_activ_rate):
        
        activation_rate=k/(nb_activ_rate)#nb_activ_rate

        path="/home/projet12/PAr135/intermittent_fault/activation_rate"+str(activation_rate)

        if not os.path.exists(path):
            os.makedirs(path)
    #change faulty line
        list_of_sample =[]
        for index in range(nb_of_intermittent_fault):
            nb_of_vect_to_change=int((1-activation_rate)*len(faulty_line))
            sample = rd.sample(faulty_line,nb_of_vect_to_change)

            if sample not in list_of_sample:
                list_of_sample.append(sample) 

        print(list_of_sample)
        for elem1 in list_of_sample:
            for elem2 in range(len(elem1)):
                matrix_copy[elem1[elem2],:] = right_matrix[elem1[elem2],:,0]
                
            final_label=np.concatenate([final_label,np.array([i])]) #change faulty line selected into right ones
            final_matrix=np.concatenate([final_matrix,matrix_copy],axis=0)
            
            matrix_copy= np.copy(matrix_data[:,:,i])
            matrix_copy= np.reshape(matrix_copy,(1,55,108))
        

        os.chdir(path)
        np.savez_compressed(filename,matrix=final_matrix,label=final_label)