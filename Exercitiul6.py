import numpy as np
x = np.array(range(15)).reshape(5,3)
print("Matrice inainte de normalizare")
print(x)
print("..............................")

col_min = x.min(axis=0)#Minimul din fiecare coloana
col_max = x.max(axis=0)#Maximul din fiecare coloana
x_norm = (x- col_min)/ (col_max - col_min)#Formula pentru normalizare(broadcasting)
print("Matrice dupa normalizare")
print(x_norm)