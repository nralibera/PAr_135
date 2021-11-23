# -*- coding: utf-8 -*-
#!/usr/bin/python2.7
"""
Created on Wed Oct 20 21:13:39 2021

@author: Nanto RALIBERA
"""

import subprocess as sb

#give the circuit path to simulate it
#circuit_path = "path_here"

#simulate the circuit
#sb.run(["cd "+circuit_path,"source /opt/source.synopsys"," tmax -s atpg.sh",])


#retrieve the right matrix and the list of fault
fault_list =[]
equivalent_faults = open("equivalent_fault.txt", "r")
fault_file = equivalent_faults.readlines()
equivalent_faults.close()

for fault in fault_file:
    fault_list.append(fault.replace(" ","").replace("\n","")) #delete all spaces in the string
    

#building the right matrix
right_matrix =[]
matrix_file_opened = open("c7552.stil", "r")
matrix_file = matrix_file_opened.readlines()
matrix_file_opened.close()

ligne = matrix_file[22].replace(" ","")
right_matrix_file = open("right_matrix.txt","w")


for i in range(0, 163, 3):
    ligne = matrix_file[250+i].replace(" ","").replace("H","1").replace("L","0").replace(";","").replace("}","")
    right_matrix.append(ligne[6:].replace("\n",""))
    right_matrix_file.write(ligne[6:])

right_matrix_file.close()

#**********************Simuling each fault***********************
open("fault_matrix_file2.txt","w").close()

file_name=""

for f in fault_list:
    fault = f.replace("\t","")[3:]
    SA = f[2]
    first_fault = fault.split(";")[0]
    file_name = "datalog_"+f[0:3].upper()+"_"+first_fault+".txt"
    file_name = file_name.replace("/","_")
    
    # simulation_file = open("fault_sim_datalog_diagnosis.sh", "w")
    # simulation_file.write("read_netlist CORE65GPSVT_tmax.v -library\n"+ #change fault_sim_datalog_diagnosis.sh to simulate fault
    #                         "read_netlist c7552_65n.v\n"+
    #                         "run_build_model c7552\n"+
    #                         "run_drc\n"+
    #                         "set_faults -model stuck\n"+
    #                         "add_faults -all\n"+
    #                         "set_patterns -external c7552.stil -sensitive\n"
    #                         "run_simulation -pin { "+ first_fault +" "+ SA +" } > "+file_name+"\n"+
    #                         "quit"
    #                         )
    # simulation_file.close()
    
    # #linux command to run tetramax
    # sb.run(["cd /home/par137/C7552_example/test2"],shell=True)
    # sb.run(["tmax -s fault_sim_datalog_diagnosis.sh"],shell=True)
    
    changes_file = open(file_name,"r")
    list_of_change =changes_file.readlines()
    changes_file.close() 
    
    fault_matrix_file2 = open("fault_matrix_file2.txt","a") #file in which the fault's matrix will be saved
    fault_matrix_file2.write(fault+ "\t"+ "SA" + SA + "\n")
    
    index = 1
    fault_matrix = []

    
    #change the right matrix in order to obtain the fault's matrix
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
    

    for elem in right_matrix:
        fault_dict = dict(zip(list_output,elem)) 
        fault_matrix.append(fault_dict)
    
    print(fault_matrix[0])
    while list_of_change[index].replace(" ","")[0:19] != "Simulationcompleted":
        i=0
        while list_of_change[index][i] == " ":
            i+=1
            
        line = list_of_change[index][ i :]
        line = line.split("  ")
        nb_line=int(line[0])
        output_name=line[1]
        output_value=int(line[2][12])

        fault_matrix[nb_line][output_name]=output_value
        index+=1
    
    #save the fault_matrix in a file
    for dictionnary in fault_matrix:
        for output in list_output:
            fault_matrix_file2.write(str(dictionnary[output]))
        fault_matrix_file2.write("\n")
    
    fault_matrix_file2.close()
