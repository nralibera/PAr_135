import numpy as np

right_matrix =[]
right_matrix_array=np.zeros((55,109),dtype=bool)
matrix_file_opened = open("c7552.stil", "r")
matrix_file = matrix_file_opened.readlines()

matrix_file_opened.close()
ligne = matrix_file[22].replace(" ","")


for i in range(0, 163, 3):
    ligne = matrix_file[250+i].replace(" ","").replace("H","1").replace("L","0").replace(";","").replace("}","")
    ligne_ajout=ligne[6:].replace("\n","")
    for j in range(len(ligne_ajout)):
        right_matrix_array[i//3,j]=int(ligne_ajout[j])


np.save("right_matrix_array",right_matrix_array)

        