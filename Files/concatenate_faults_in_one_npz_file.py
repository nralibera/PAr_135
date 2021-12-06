# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 08:14:21 2021

@author: Utilisateur
"""
#Concatenating all faults in one matrix and label
import numpy as np
from tqdm import tqdm

nb_array=3609
matrix_file=np.load('intermittent_fault_file_compressed/intermittent_fault_array0.npz')
matrix_all_faults=matrix_file['matrix']
labels_all_faults=matrix_file['label']
L_matrix=[]
L_label=[]
for k in tqdm(range(1,nb_array)):
  compressed_file_name="intermittent_fault_array"+str(k)
  matrix_file= np.load("intermittent_fault_file_compressed/"+compressed_file_name+ ".npz")
  L_matrix.append(matrix_file['matrix'])
  L_label.append(matrix_file['label'])
  
matrix_all_faults = np.concatenate(L_matrix,axis=2)
labels_all_faults = np.concatenate(L_label)
np.savez_compressed('matrix_all_faults_compressed',matrix=matrix_all_faults,label=labels_all_faults)
#for k in range(1,4): --> i tested it works ;)