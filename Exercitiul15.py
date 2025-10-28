import numpy as np

np.random.seed(42)
A = np.random.randn(6,6)
print("Basic:",A)
detA = np.linalg.det(A)
print("Determinant:",detA)
rankA = np.linalg.matrix_rank(A)
print("Rang:",rankA)

#Inversa si verificare

if rankA == 6:
    Ainv = np.linalg.inv(A)
    print("A * A^(-1) ~~ I?", np.allclose(A @ Ainv, np.eye(6)))
else:
    print("Matricea nu are inversa")

