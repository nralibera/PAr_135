# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 23:04:52 2021

@author: Utilisateur
"""
import os
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
os.chdir("C:/Users/Utilisateur/Documents/GitHub/PAr_135/Files")

def sub_bool(a,b):
    if a :
        if b :
            return 0
        else :
            return 1
    else :
        if b :
            return 1
        else :
            return 0


def norm_1(matrix_1,matrix_2):
    distance = 0
    dimensions=np.shape(matrix_1)
    if dimensions!=np.shape(matrix_2):
        return ('Pas la même taille')
    for i in range(dimensions[0]) :
        for j in range(dimensions[1]):
            distance+=sub_bool(matrix_1[i,j],matrix_2[i,j])
    return distance

def norm_1_KNN(matrix_1,matrix_2):
    distance = 0
    dimensions=np.shape(matrix_1)[0]
    if dimensions!=np.shape(matrix_2)[0]:
        return (np.inf())
    for i in range(dimensions) :
            distance+=sub_bool(matrix_1[i],matrix_2[i])
    return distance

    
###creating training and testing data set

nb_class=6
size_fault_matrix=(int(55),int(108))
numb_coeff=int(size_fault_matrix[0]*size_fault_matrix[1])
rate_train=0.6
"""
trainset=[]
testset=[]
label=[]

for i in range (nb_class):
    file_name='intermittent_fault_file/intermittent_fault_array'+str(i)+'.npz'
    Matrix_list=np.load(file_name)['matrix']
    number_intermittent=np.shape(Matrix_list)[2]
    sample_size=int(number_intermittent*rate_train)
    Matrix_fault_test=np.zeros((sample_size,numb_coeff),dtype=bool)
    Matrix_fault_train=np.zeros((sample_size,numb_coeff),dtype=bool)
    Matrix_remodeled=np.reshape(Matrix_list,(number_intermittent,numb_coeff))
    for j in range(sample_size):
        label+=[i+1]
        Matrix_fault_train[j,:]=Matrix_remodeled[j,:]
        Matrix_fault_test[j,:]=Matrix_remodeled[number_intermittent-j-1,:]
    trainset.append(Matrix_fault_train)
    testset.append(Matrix_fault_test)
label=np.array(label,dtype=int)
matrix_trainset=np.concatenate(trainset,axis=0)
matrix_testset=np.concatenate(testset,axis=0)
np.savez_compressed('trainset_KNN',matrix=matrix_trainset,label=label) 
np.savez_compressed('testset_KNN',matrix=matrix_testset,label=label)

print('datasets are ready')

"""

"""
###Allows for less modulation of the training and testing set 
#but it is quicker to code, these lines are more like a reminder 
#that this function exist

from sklearn.model_selection import train_test_split
#split dataset into train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1, stratify=y)
"""


"""
lab = iris.loc[:,"species"]
iris = pandas.read_csv("iris.csv")
x = iris.loc[:,"petal_length"]
y = iris.loc[:,"petal_width"]

for e, c in [('setosa','g'), ('virginica', 'r'), ('versicolor', 'b')]:
    plt.scatter(x[lab == e], y[lab == e], color = c, label = e)

k = 3
d = list(zip(x,y)) # Regroupement en couples de coordonnées (x, y)
model = KNeighborsClassifier(n_neighbors = k)
model.fit(d, lab)
prediction = model.predict([[longueur,largeur]])
"""

#Run only once

trainset=np.load('trainset_KNN.npz')['matrix']
label=np.load('trainset_KNN.npz')['label']
model=KNeighborsClassifier(n_neighbors = 3,algorithm='auto',metric=norm_1_KNN)
model.fit(trainset,label)

X_test=np.load('testset_KNN.npz')['matrix']
Y_test=np.load('testset_KNN.npz')['label']
#result=model.predict(X_test)[0:5]
#true_result=Y_test[0:5]
test=model.score(X_test,Y_test)

#with only 6 class it took quite some time, 60% training set so approximately 60 
# training matrix per class --> give a 27% success rate
# plus 1/6 of test matrix were training matrix so normally 16% of test matrix 
#are already known