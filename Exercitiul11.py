import numpy as np
import time

n = int(5e6)
a,b,c = 2,3,4
x = list(range(n))
y = []

start = time.time()
for xi in x:
    y.append(a*xi**2 + b*xi + c)
end = time.time()

print("Timp bucla Python:", end - start, "secunde")
print("----------------------------------------------")

n = int(5e6)
a, b, c = 2,3,4
x = np.arange(n)

start = time.time()
y = a*x**2 +b*x + c
end = time.time()
print("Timp vectorizat NumPy:", end - start, "secunde")

