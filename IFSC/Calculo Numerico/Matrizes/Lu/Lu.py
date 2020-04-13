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
'''
O pprintmódulo fornece a capacidade de "imprimir de maneira bonita" 
estruturas de dados Python arbitrárias em um formulário que pode ser usado 
como entrada para o intérprete.
'''


def Lu(A, b):
    n = len(A)
    # 'np.asarray' converta a entrada em uma matriz.
    # dtype : tipo de dados, opcional
    A, b = np.asarray(A, dtype=np.float64), np.asarray(b, dtype=np.float64)
    # 'numpy.identity' (n, dtype = None): retorna uma matriz de identidade,
    # ou seja, uma matriz quadrada com as do daignol principal.
    L = np.asarray(np.identity(n))
    U = np.copy(A)
    P = np.identity(n)

    '''
    'numpy.argsort()' A função é usada para executar uma classificação indireta 
    ao longo do eixo especificado, usando o algoritmo especificado pela 
    palavra-chave kind. Ele retorna uma matriz de índices da mesma forma que 
    arrey que ordenaria a matriz. Inverte a posição da diagonal! (Identidade)
    
    permutation = abs(U[:, 0]).argsort()[::-1]
    U = U[permutation]
    P = P[permutation]
    '''

    for k in range(n):  # para cada coluna de A em Ab
        # Eliminação direta - subtraindo linhas
        for j in range(k + 1, n):  # Para cada linha em diagonal da k coluna
            # calcular a relação com o valor na diagonal principal
            main_diagonal = float(U[j][k]) / U[k][k]

            L[j][k] = main_diagonal

            for m in range(k, n):  # para cada coluna em uma linha j
                # Ab[j][m] -=  main_diagonal * Ab[k][m]   #calcule Rj - main_diagonal*Rk.  Isso resultará em todos os zeros abaixo da diagonal principal
                if m < len(U):
                    U[j][m] -= main_diagonal * U[k][m]

    # numpy.zeros (shape, dtype = None, order = 'C'): Retorna uma nova matriz de
    # determinado formato e tipo, com zeros.
    #x = np.zeros(n)
    #print(f'\nDEBUG: {x}\n')

    # Triângulo superior de uma matriz. Retorne uma cópia de uma matriz com os
    # elementos abaixo da k- ésima da diagonal zerados.
    U = np.triu(U)

    # Interprete a entrada como uma matriz. Ao contrário matrix, asmatrixnão
    # faz uma cópia se a entrada já for uma matriz ou um ndarray. Equivalente
    # a .matrix(data, copy=False)
    return (np.asmatrix(L), np.asmatrix(U), np.asmatrix(P))
