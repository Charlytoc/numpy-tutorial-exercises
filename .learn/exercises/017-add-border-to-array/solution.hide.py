import numpy as np

matrix = np.ones((3, 3))

padded_matrix = np.pad(matrix, pad_width=1)


print(padded_matrix)
