import numpy as np

x = np.array(range(200))
print(x.dtype)
d=  np.clip(x, 0 ,100)
np.unique(d)
print("Array.ul in care valorile mai mici decat 0 devin 0 si cele mai mari de 100 devin 100")
print(d)# varianta in care toate valorile de trec 100 devin 100 dar range-ul e tot 200
print("--------------------------------------------------------------------")
print("Limitarea 0- 100")
d1 = np.where(x <= 100) # tot ce trece de 100 nu mai apare in noul array
print(d1)