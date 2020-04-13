# -*- coding: utf-8 -*-
"""
Criado por: 
@author: Kevin Corcor
Editado por:
bed72 - Gabriel Ramos

Observe que a matriz de resultados começa na última variável
ou seja: x [3.0, 5.0, 7.0] significa x3 = 3, x2 = 5.0, x1 = 7.0 e assim por diante.

@author: Kevin Corcor
Link: https://github.com/KevinCorcor/Numerical-Computation/blob/master/python/GE_LU.py
"""


from pprint import pprint
import numpy as np
import Lu as decomposition

'''
O pprintmódulo fornece a capacidade de "imprimir de maneira bonita" 
estruturas de dados Python arbitrárias em um formulário que pode ser usado 
como entrada para o intérprete.
'''
A = np.array([
    [9, -6, -3, -4, -5, -5, -8, 6, -2, 2, -7, -1, 4, -9, 4, 5, 9, 4, 9, -5],
    [-8, 5, -7, -8, 0, 2, 10, -8, -2, -8, 10, -2, -10, 2, 7, -7, 6, -8, -4, -8],
    [0, -1, -3, 9, -5, -4, -7, 8, 0, -3, -1, -2, -8, 10, -1, 5, -9, 10, 1, -9],
    [9, -10, 7, -10, -4, 7, 4, 9, 9, -2, 2, 10, -2, 1, 2, 8, 4, -4, 6, 5],
    [-6, -8, -4, 3, 0, 6, 4, -3, 3, -5, -2, -7, -9, -10, 8, 0, -9, -7, 3, 0],
    [8, 1, 5, -1, -7, 6, -6, -8, -7, 8, 6, 2, -6, -7, 5, 7, -9, -6, 3, -9],
    [7, 1, 3, -6, -9, 4, 0, 5, -4, -2, -2, -2, -6, 0, -6, 0, 4, -3, 0, -6],
    [-8, 6, -1, -9, 0, -10, -10, -10, 5, -10, -2, 4, -10, 2, 7, 1, -5, -6, 0, -4],
    [7, -2, -8, -5, -2, -9, 10, -7, -8, -2, 5, 2, 3, -3, 4, -10, 10, 5, 4, -5],
    [7, -9, 6, 5, 5, -6, -3, -3, 1, -4, 0, -6, 10, 0, 7, 8, -5, 10, -4, -3],
    [6, -9, 4, 5, -1, -5, 10, 10, -8, 9, 3, 9, -9, 6, -10, 5, -1, -7, -5, 3],
    [4, 3, -10, -1, -3, 5, 4, -10, 2, -8, -4, 9, 7, 7, 6, -3, 1, -4, -6, 2],
    [7, 10, 10, 2, 6, -7, 10, 1, 2, 6, -6, 8, 6, 10, 1, -1, 7, -2, 5, 9],
    [-7, 9, 9, -3, 10, 4, 6, 3, -9, -2, -6, -4, -6, 3, -8, -6, 7, 1, 8, -9],
    [1, 1, -4, -4, -4, 1, -5, -6, -4, -1, 5, 7, -2, -5, 9, -2, 0, 4, 3, -8],
    [5, 0, -10, -6, -7, -1, 8, 4, 1, -10, 4, -9, -4, -7, -4, 3, 5, 8, 2, 6],
    [-10, -2, 10, 7, -7, 5, -8, 6, 5, 8, 9, -7, -5, -10, 7, -1, -2, -4, 2, 7],
    [-6, 6, 1, 4, 0, -2, 3, -8, 9, -6, 7, -6, -4, -2, 10, 7, 10, 1, 1, 2],
    [1, -8, 8, -9, 10, 7, -5, 5, -2, -9, 10, 5, 6, 0, -8, -8, -3, 7, -7, -1],
    [6, 9, -7, -4, -2, 0, 3, 1, -9, -7, 0, -8, 1, -5, -8, -4, 10, -3, 8, 6]
])


b = [
    [-15.13620337],
    [-39.00404466],
    [97.77414194],
    [77.49451566],
    [88.98422281],
    [-30.08865658],
    [-31.79366138],
    [2.706242335],
    [-47.27926512],
    [28.16297901],
    [-2.672380611],
    [-22.54696639],
    [-2.54743802],
    [-146.1374418],
    [-33.24042277],
    [-22.63040472],
    [154.6761739],
    [9.713142717],
    [-57.9061427],
    [-126.9036292]
]

L, U, P = decomposition.Lu(A, b)

print('-=' * 60)
print('\nL: ')
pprint(L)
print('\nU: ')
pprint(U)
print('\nIdentidade: ')
pprint(P)
print()
print('-=' * 60)

# Ly = b
bb = np.asmatrix(P) * np.asmatrix(b)
print('\nLy = b: \n')
pprint(bb)
print()
print('-=' * 60)

n = len(L)
#Lb = np.asarray(np.c_[L, bb],dtype=np.float64)

y = np.zeros(n)
for i in range(n):
    y[i] = bb[i]
    for j in range(i):
        y[i] -= L[i, j] * y[j]
    y[i] = y[i] / L[i, i]
# Interprete a entrada como uma matriz.
y = np.asmatrix(y).T

print(f'\ny: \n')
pprint(y)
print()
print('-=' * 60)

# Ux = y
x = np.zeros(n)
Uy = np.asarray(np.c_[U, np.asarray(y)], dtype=np.float64)
# Backwards Substitution - Resolva uma variável e substitua-a novamente para resolver outra
# simplesmente resolva a última linha, pois deve haver apenas uma desconhecida
x[n - 1] = float(Uy[n - 1][n]) / Uy[n - 1][n - 1]
# start, stop, step - a partir da segunda última linha, faça o backup das linhas
for i in range(n - 1, -1, -1):
    z = 0.0  # deixe ou redefina para 0
    for j in range(i + 1, n):  # for each column in a Row j
        # substitua as respostas de baixo (armazenadas em x) na equação da linha atual
        z = z + float(Uy[i][j]) * x[j]
    # resolver para esta linha, onde agora deve haver apenas um desconhecido
    x[i] = float(Uy[i][n] - z) / Uy[i][i]
x = np.asmatrix(x).T
print(f'\nO resultade é: \n\nCUIDADO ORDEM INVERSA DE BAIXO PARA CIMA: \nXn -> ... -> X3 -> X2 -> X1: \n')
pprint(x)
print()
print('-=' * 60)
