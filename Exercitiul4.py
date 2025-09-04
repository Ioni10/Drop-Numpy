#Diferențe finite: pentru x = [0, 0.5, ..., 5], calculează np.diff de ordin 1 și 2; interpretează.
import numpy as np
x = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
# np.diff gaseste diferentele dintre numerele consecutive din array
y = np.diff(x,n=1) # Cand ii spunem n= 1 -> facem referinta la ordinul 1
z = np.diff(x, n=2)# Cand ii spunem n = 2 -> facem de 2 ori diferenta adica mai facem odata cu a2a lista data

print("Array original",x)
print("Diferenta de ordin 1",y)
print("Diferenta de ordin 2",z)