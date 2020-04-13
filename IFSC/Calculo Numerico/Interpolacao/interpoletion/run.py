import numpy as np
import Gauss as gss

matrix = np.array([
    [2.8**2, 2.8, 1],
    [3.0**2, 3.0, 1],
    [3.2**2, 3.2, 1]
])

b = np.array([
    [16.44],
    [20.08],
    [24.53]
])

gss.gauss_interpolation(matrix, b)
