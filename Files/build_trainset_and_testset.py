# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 23:21:55 2021

@author: Nanto RALIBERA
"""
import numpy as np
import random as rd
from tqdm import tqdm

data=np.load("data.npz")

matrix_data = data['matrix']
label = data["label"]//30 #to have 120 superclass

train_index=[]
test_index=[]

for i in tqdm(range(matrix_data.shape[2])):
  if rd.random()<0.8:
    train_index.append(i)
  else:
    test_index.append(i)


#training data

x_train_list = [np.reshape(matrix_data[:,:,i],(55,108,1)) for i in train_index]
x_train = np.copy(x_train_list[0])
x_train = np.concatenate(x_train_list,axis = 2)

y_train_list = [np.array([label[i]]) for i in train_index]
y_train = np.copy(y_train_list[0])
y_train = np.concatenate(y_train_list)

#test data
x_test_list = [np.reshape(matrix_data[:,:,i],(55,108,1)) for i in test_index]
x_test = np.copy(x_test_list[0])
x_test = np.concatenate(x_test_list,axis = 2)

y_test_list = [np.array([label[i]]) for i in test_index]
y_test = np.copy(y_test_list[0])
y_test = np.concatenate(y_test_list)

#np.savez_compressed("dataset",x_train=x_train,y_train=y_train,x_test=x_test,y_test=y_test)
#print(x_train.shape,y_train.shape,x_test.shape,y_test.shape)