import numpy as np
x = np.arange(10)
y = np.arange(10, 0, -1)
print(x)
print(y)

produs_scalar = np.dot(x,y)
norma_x = np.linalg.norm(x)
norma_y = np.linalg.norm(y)
cos_theta = np.dot(x,y) / (np.linalg.norm(y) * np.linalg.norm(x))
theta = np.arccos(cos_theta)
print(theta)
print(np.degrees(theta))

