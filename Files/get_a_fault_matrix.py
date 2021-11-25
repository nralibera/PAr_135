# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 11:56:25 2021

@author: Nanto RALIBERA
"""
right_matrix =[]
matrix_file = open("c7552.stil", "r").readlines()
ligne = matrix_file[22].replace(" ","")

for i in range(0, 163, 3):
    ligne = matrix_file[250+i].replace(" ","").replace("H","1").replace("L","0").replace(";","").replace("}","")
    right_matrix.append(ligne[6:].replace("\n",""))


list_output="N387, N388, N478, N482, N484, N486, N489, N492, N501, N505, N507,\
    N509, N511, N513, N515, N517, N519, N535, N537, N539, N541, N543,\
     N545, N547, N549, N551, N553, N556, N559, N561, N563, N565, N567,\
     N569, N571, N573, N582, N643, N707, N813, N881, N882, N883, N884,\
     N885, N889, N945, N1110, N1111, N1112, N1113, N1114, N1489, N1490,\
     N1781, N10025, N10101, N10102, N10103, N10104, N10109, N10110, N10111,\
     N10112, N10350, N10351, N10352, N10353, N10574, N10575, N10576,\
     N10628, N10632, N10641, N10704, N10706, N10711, N10712, N10713,\
     N10714, N10715, N10716, N10717, N10718, N10729, N10759, N10760,\
     N10761, N10762, N10763, N10827, N10837, N10838, N10839, N10840,\
     N10868, N10869, N10870, N10871, N10905, N10906, N10907, N10908,\
     N11333, N11334, N11340, N11342, N241_O".replace(" ","").split(",")

list_of_change = open("datalog_SA1_N23.txt").readlines()
index = 1
fault_matrix = []
 
for elem in right_matrix:
   fault_dict = dict(zip(list_output,elem)) 
   fault_matrix.append(fault_dict)
   
while list_of_change[index].replace(" ","")[0:19] != "Simulationcompleted":
    i=0
    while list_of_change[index][i] == " ":
        i+=1
        
    line = list_of_change[index][ i :]
    line = line.split("  ")
    fault_matrix[int(line[0])][line[1]]=int(line[2][12])
    index+=1

n23_matrix=open("n23_matrix.txt","w")

for dictionnary in fault_matrix:
    for key,content in dictionnary.items():
        n23_matrix.write(str(content))
    n23_matrix.write("\n")
    
n23_matrix.close()