import numpy as np

np.random.seed(1)
s = np.random.normal(10,2,1000)
media = s.mean()
std = s.std()
y = 100 * np.mean((s >= 6) & (s <= 14))
print("loc=10, scale=2, random 1000:")
print(s)
print("-----------------------------------------")

print("Media numerelor random:")
print(media)
print("-----------------------------------------")

print(f"Deviatia standard:")
print(std)
print("------------------------------------------------------")
print("Procentul din [6,14]:", y,"%")
