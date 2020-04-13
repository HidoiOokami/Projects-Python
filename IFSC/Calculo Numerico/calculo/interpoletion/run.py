import numpy as np
import Gauss as gss

matrix = np.array([[7, 11.25, 23.3125], [11.25, 23.3125, 55.546875],
                   [23.3125, 55.546875, 142.5039063]])

b = np.array([[8.9], [14.025], [32.59375]])

f = 3

gss.gauss_interpolation(matrix, b, f)
