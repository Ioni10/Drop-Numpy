import numpy as np


A = np.array([[1,2,3],
              [4,5,6]])

B = np.array([[7,8],
             [9,10],
             [11,12]])

kronecker = np.kron(A,B)

print('A= \n',A)
print('B= \n',B)
print('Produsul Kronecker= \n',kronecker)

#----------Hadamard

A2 = np.array([[1,2,3],
              [4,5,6]])

B2 = np.array([[2,2,2],
               [3,3,3]])

hadmarad = A2 * B2
print('Produsul Hadamard = \n', hadmarad)