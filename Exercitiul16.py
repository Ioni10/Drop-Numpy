import numpy as np

np.random.seed(42)
A = np.random.randn(5,5)
b = np.random.randn(5)
x = np.linalg.solve(A,b)

eroare = np.linalg.norm(A @ x -b, ord=2)

print("Matrice:",A)
print("Vector:",b)
print("Solutia",x)
print("Eroarea:",eroare)