#Indexare booleană: matrice 10×10 U(0,1); setează la NaN elementele &lt;0.2; numără NaN.
import numpy as np
matrice = np.random.rand(10,10)
print(matrice)
masca = matrice < 0.2
matrice[masca] = np.nan
print("Matricea cu NaN-Uri:", matrice)
numar_nan = np.isnan(matrice).sum()
print("Numarul de NaN-uri:", numar_nan)
