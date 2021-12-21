# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 14:59:02 2021

@author: Utilisateur aka Kévin-Lâm
"""
# importing modules
import numpy as np
from tqdm import tqdm
import time as t
##variables
nb_class=3609
size_fault_matrix=(55,108)

t1=t.time()
def norme_1(matrix_1,matrix_2):
    distance = 0
    dimensions=np.shape(matrix_1)
    if dimensions!=np.shape(matrix_2):
        return ('Pas la même taille')
    for i in range(dimensions[0]) :
        for j in range(dimensions[1]):
            distance+=abs(int(matrix_1[i,j])-int(matrix_2[i,j]))
    return distance

##regroup all permanent fault in the same matrix --> easier to operate on them
"""
matrix_file_opened= open('fault_matrix_file2.txt',"r")
matrix_file=matrix_file_opened.readlines()
matrix_grouped=np.zeros((size_fault_matrix[0],size_fault_matrix[1],nb_class),dtype=bool)
for k in tqdm(range(nb_class)):
    for cpt in range(size_fault_matrix[0]):
        for j in range(size_fault_matrix[1]):
            matrix_grouped[cpt,j,k]=int(matrix_file[(k+1)+k*size_fault_matrix[0]+cpt][j])

np.savez_compressed('permanent_fault',matrix=matrix_grouped)
"""
###Creation de classe :

nb_metaclass=120
avg_element_per_class=nb_class//120


# easy method: we take the first avg_element_per_class closest matrix to the first matrix 
# then we do the same for the second etc.





already_classified=np.zeros((nb_class),dtype=bool)
metaclassnumber=0

matrix_permanents=np.load('permanent_fault.npz')['matrix']
List_metaclass= {}
for i in tqdm(range(nb_class)): # we create a sorted list of elements
    if not already_classified[i]:
        L_chosen=[]
        L_chosen.append(i)
        already_classified[i]=True
        metaclassnumber+=1
        print(metaclassnumber)
        studied_matrix=matrix_permanents[:,:,i]
        L_dist=[]
        for j in range(i,nb_class):
            if not already_classified[j]:
                L_dist.append((norme_1(studied_matrix,matrix_permanents[:,:,j]),j))
        L_dist.sort() #a way to improve is to add element at the right place 
        #so the list remain always sorted, (we can use dichotomy to add the dist at the right
        #place)

        for chosen in range(min(avg_element_per_class-1,len(L_dist))):
            L_chosen.append(L_dist[chosen][1])
            already_classified[L_dist[chosen][1]]=True
        List_metaclass["class%s" %metaclassnumber] = L_chosen


t2=t.time()
duration=t2-t1   
     
#To optimize There is nb_class! distances to calculate then we can sort it ?
#and the we classify each matrix according to those distances
