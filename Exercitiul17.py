import numpy as np


np.random.seed(42)

A = np.random.randn(4,4)
A = (A + A.T)/2

valori, vectori = np.linalg.eigh(A)


A_reconstruit = vectori @ np.diag(valori) @ vectori.T

eroare = np.linalg.norm(A - A_reconstruit, ord='fro')

print("Matrice:", A)
print("Valorile:", valori)
print("Vectorii:", vectori)
print("Matrice recompusa:", A_reconstruit)
print("Eroarea:", eroare)

