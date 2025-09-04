import numpy as np
#2) Aranjamente și reshaping: array 3×4 cu valori 0..11; reshape la 2×6 și 4×3; explică ordinea C vs F.
vector = np.arange(12)
matrice = vector.reshape(3, 4)
matrix = matrice.reshape(2 , 6)
print("----(3,4)------")
print(matrice)
print("-----(2,6)-----")
print(matrix)
print("------(4,3)-----")
print(matrix.reshape(4,3))
#Ordinea e .reshape(Coloana , Rand)

