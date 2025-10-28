import numpy as np
import time

np.random.seed(42)
n = 1_000_000
k = 10

a = np.random.randn(n)

t0 = time.perf_counter()
idx_topk_unordered = np.argpartition(a, -k)[-k:]
t1 = time.perf_counter()

topk_values = a[idx_topk_unordered]
order_desc = np.argsort(topk_values)[::-1]
idx_topk_sorted = idx_topk_unordered[order_desc]
topk_sorted_values = topk_values[order_desc]
t2 = time.perf_counter()

print(f'Generare + argpartition: {t1-t0:.4f} s')
print(f"Sortare top-k (k={k}): {t2-t1:.6f} s")
print("\nTop-10 (descrescator) valori si indexi in vectorul original:")
for rank, (idx, val) in enumerate(zip(idx_topk_sorted, topk_sorted_values), start=1):
    print(f"{rank:2d}. index={idx:7d}  value={val:.6f}")

for rank, (idx, val) in enumerate(zip(idx_topk_sorted, topk_sorted_values), start=1):
    print(f"{rank:2d}. index={idx:7d} value={val:.6f}")