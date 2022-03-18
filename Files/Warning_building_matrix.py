# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 20:48:03 2022

@author: Utilisateur
"""
import numpy as np

A=np.zeros((55,108,3609))
B=A[:,:,1500]
print(np.shape(B))
B[0,0]=1
print(A[0,0,1500]) #--> attention a utiliser copy car meme espace memoire pour B et A
