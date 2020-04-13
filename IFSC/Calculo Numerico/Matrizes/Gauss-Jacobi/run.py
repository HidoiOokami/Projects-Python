# -*- coding: utf-8 -*-
"""
Criado por: 
bed72 - Gabriel Ramos
"""
import numpy as np
import math
import Gauss_Jacobi as gsj

precision = math.pow(10, -4)

matrix = np.array([
    [-4.1, 1.8, 0.7, -1.2, -3.2],
	[0.9, 3.8, -1.1, 0.8, 8.4],
	[-1.4, -1.1, 4.4, 0.5, 11.6],
	[-1.3, 2.1, -0.2, -5.1, -18.1]
])

x0 = np.array([0, 0, 0, 0])


print(f'\nO resultade é: \n\n')

gsj.gauss_jacobi(matrix, x0, precision)


print('-=' * 60)
