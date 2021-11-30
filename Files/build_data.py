# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 09:33:33 2021

@author: Nanto RALIBERA
"""

import numpy as np
import random as rd
from tqdm import tqdm

def write_matrix_in_a_file(matrix,label,file_name):
    file_name.write(label+"\n")
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            file_name.write(str(matrix[i,j,0]))
        file_name.write("\n")

    
    
# def idx2fault(idx):
#     fault_list_file=open("equivalent_fault.txt","r")
#     fault_list=fault_list_file.readlines()
#     fault_list=[j.replace("\n","") for j in fault_list]
#     fault_list_file.close()
#     return fault_list[idx]


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


def build_intermittent_fault(right_matrix,matrix_data,label,activation_rate=0.85,nb_of_intermittent_fault=50,):
    #building intermitent fault
    for i in range(1):#range(matrix_data.shape[2]):
        faulty_line=[]
        matrix_copy= np.copy(matrix_data[:,:,i])
        matrix_copy= np.reshape(matrix_copy,(55,108,1))
        for j in range(matrix_data.shape[0]): #get the faulty lines
            for k in range(108):
                if  matrix_copy[j,k,0] != right_matrix[j,k,0]:
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
                matrix_copy[elem1[elem2],:,0] = right_matrix[elem1[elem2],:,0]
            write_matrix_in_a_file(matrix_copy,"intermittent_fault.txt")
            label=np.concatenate([label,np.array([i])])
            matrix_data=np.concatenate([matrix_data,matrix_copy],axis=2)
    return matrix_data,label

#Opening the fault_list
fault_list_file=open("equivalent_fault.txt","r")
fault_list=fault_list_file.readlines()
fault_list=[j.replace("\n","") for j in fault_list]
fault_list_file.close()


#building the right_matrix
right_matrix_file=open("right_matrix.txt","r")
right_matrix = build_matrix(right_matrix_file.readlines())
right_matrix_file.close()

#building permanent_fault
matrix_data,label,list_fault = build_data("fault_matrix_file2.txt")
# open("intermittent_fault.txt","w").close()


#building intermitent fault
#file for the intermittent fault
intermittent_file=open("intermittent_fault2.txt","a")

activation_rate = 0.85 #85% des vecteurs de la faute permanente restent intacts le reste est remplacés
nb_of_intermittent_fault=100

for i in tqdm(range(1366,3608)):
    faulty_line=[]
    matrix_copy= np.copy(matrix_data[:,:,i])
    matrix_copy= np.reshape(matrix_copy,(55,108,1))
    for j in range(matrix_data.shape[0]): #get the faulty lines
        for k in range(108):
            if  matrix_copy[j,k,0] != right_matrix[j,k,0]:
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
            matrix_copy[elem1[elem2],:,0] = right_matrix[elem1[elem2],:,0]
        write_matrix_in_a_file(matrix_copy,fault_list[i],intermittent_file)
        # label=np.concatenate([label,np.array([i])])
        # matrix_data=np.concatenate([matrix_data,matrix_copy],axis=2)

intermittent_file.close()





"""print(len(list_fault))
print(label)
print(np.shape(matrix_data))"""

