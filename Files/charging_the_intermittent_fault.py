# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 09:38:51 2021

@author: Nanto RALIBERA
"""

import numpy as np
import random as rd
from tqdm import tqdm


matrix_list =[]
label_list = []
for i in tqdm(range(3609)):
    file=np.load("intermittent_fault_array"+str(i)+".npz")
    matrix_list.append(file['matrix'])
    label_list.append(file['label'])
    

matrix = matrix_list[0]
matrix = np.concatenate(matrix_list,axis=2)

label = label_list[0]
label = np.concatenate(label_list)
