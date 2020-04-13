from math import sqrt
import numpy as np
from numpy import array
from numpy.linalg import cholesky

# define a 3x3 matrix
A = np.array([
    [8, -1, 0.5, 2.1, -1.2, 17.461],
    [-1, 9, -1.2, 3.1, 0.5, 10.025 ],
    [0.5, 1.2, 6, -0.4, -1.5, -17.386],
    [2.1, -3.1, -0.4, 8, 1, 1.103],
    [-1.2, 0.5, 1.5, 1, 6, 0.285]
])

# Cholesky decomposition
L = cholesky(A)
print(L)
print(L.T)
# reconstruct
B = L.dot(L.T)
print(f'Matriz A:\n{B}\n')
