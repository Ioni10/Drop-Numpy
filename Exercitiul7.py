import numpy as np
#x = np.array(range(36)).reshape(6,6)
y = np.zeros((6,6))# Creaza o matrice de 6 coloane 6 randuri plina de 0.uri
np.fill_diagonal(y,1)# insereaza valoarea in matricea selectata pe diagonala
np.fill_diagonal(y[1:], 2)# aici i-am explicat comenzi ca vrem cu 1 dedesupt
np.fill_diagonal(y[:,1:],2)#Deasupra
print(y)