# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 14:59:02 2021

@author: Utilisateur aka Kévin-Lâm
"""
# importing modules
import numpy as np

##variables
nb_class=3609
size_fault_matrix=(55,108)


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
matrix_file_opened= open('fault_matrix_file2.txt',"r")
matrix_file=matrix_file_opened.readlines()
matrix_grouped=np.zeros((size_fault_matrix[0],size_fault_matrix[1],nb_class),dtype=bool)
for k in range(nb_class):
    for cpt in range(size_fault_matrix[0]):
        for j in range(size_fault_matrix[1]):
            matrix_grouped[cpt,j,k]=int(matrix_file[(k+1)+k*size_fault_matrix[0]+cpt][j])
np.savez_compressed('permanent_fault',matrix_grouped)
###Creation de classe :
"""
nb_metaclass=120
avg_element_per_class=nb_class//120


# easy method: we take the first avg_element_per_class closest matrix to the first matrix 
# then we do the same for the second etc.





already_classified=np.zeros((nb,nb_class))
already_classified[0]=1



for i in range(nb_class):
    matrix_etudier=np.zeros 
    for j in range(i,nb_class):
        
#To optimize There is nb_class! distances to calculate then we can sort it ?
#and the we classify each matrix according to those distances
"""