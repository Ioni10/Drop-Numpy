import numpy as np

np.random.seed(42)

img = np.random.randint(0,256, (20,20))

kernel = np.ones((3,3))/9

img_pad = np.pad(img, 1, mode='constant')

blur = sum(
    kernel[i, j] * img_pad[i:i+20, j:j+20]
    for i in range(3)
    for j in range(3)
)

print("Imagine blur (20x20):")
print(np.round(blur, 1))

