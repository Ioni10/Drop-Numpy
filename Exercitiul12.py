import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9,10])
kernel = np.ones(5) /5
y= np.convolve(x, kernel, mode='same')

print(y)
