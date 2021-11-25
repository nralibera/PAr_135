# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 19:23:45 2021

@author: Nanto RALIBERA
"""

equiv=[]

f = open("c7552.fault","r")
    
i=0;
matrix=0
lines = f.readlines()
open("equivalent_fault.txt", 'w').close()
equiv_fault = open("equivalent_fault.txt",'a')
lines = [line.replace("\n","").replace(" ","") for line in lines]
equiv_fault.write(lines[0][0:3]+"\t"+lines[0][5:])

lines = lines[1:]

for line in lines:
    print (line)
    if line[3:5]=="DS":
        equiv_fault.write("\n"+line[0:3]+"\t"+ line[5:])
    else:
        equiv_fault.write(";"+line[5:])
        
f.close()
 
equiv_fault.close()
