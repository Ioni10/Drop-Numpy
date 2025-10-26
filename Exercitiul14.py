import numpy as np

np.random.seed(42)

data = np.random.randn(8,4) * 10
data[2,1] = np.nan
data[4,3] = np.nan
data[5,0] = np.nan
data[7,2] = np.nan

print("Original:\n", np.round(data, 2))

mediane = np.nanmedian(data, axis=0)
inds_nan = np.isnan(data)
data[inds_nan] = np.take(mediane, np.where(inds_nan)[1])

print("Imputare mediana:\n", np.round(data, 2))