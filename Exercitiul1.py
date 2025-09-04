import numpy as np
#1) Vectori de bază: creează un vector 0..9, extrage elementele pare, calculează sumă/media/abaterea standard.
arr = np.arange(10)
par = arr[arr%2==0]
print(arr)
print("Numerele pare din Vector", par)
#Suma
suma = np.sum(par)
print("Suma numerelor pare din Vector",suma )
#Media
media = np.mean(par)
print("Media numerelor pare din Vector", media)
#Abatere standard
abatere = np.std(par)
print("Abaterea standard a numerelor pare din Vector", abatere)

