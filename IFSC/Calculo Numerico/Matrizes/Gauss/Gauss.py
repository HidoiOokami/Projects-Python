# -*- coding: utf-8 -*-
"""
Criado por:
@author: Jediyanu Wigas Tu'u, dia: Qua 21/12 12:11:32 2016
Editado por:
bed72 - Gabriel Ramos

Observe que a matriz de resultados começa na última variável
ou seja: x [3.0, 5.0, 7.0] significa x3 = 3, x2 = 5.0, x1 = 7.0 e assim por diante.

@author: Jediyanu Wigas Tu'u
Link: https://github.com/jwigas/gaussElimination
"""
import numpy as np


# O formulário da matriz já deve estar no formato [A | b]
# Onde 'A' é o sistema e 'b' é a saída
def gauss(matrix):
    # Garantindo uma matriz, asarray converte a entrada em uma matriz
    np.asarray(matrix)
    # Garantindo que os dados de dada matriz sejam Flutuantes
    matrix = matrix.astype(float)

    '''
    print('-=' * 60)
    print('\nA Matriz inicial A: \n')
    print(f'{matrix}\n')
    print('-=' * 60)
    '''

    if matrix[0, 0] == 0.0:
        ''' Tratando exceção da 1° linha e coluna '''
        raise Exception("A primeira linha e coluna da matriz não podem ser 0!")

    '''
        A propriedade shape é geralmente usada para obter a forma atual de uma matriz,
        mas também pode ser usada para remodelar a matriz no local, atribuindo-lhe uma
        tupla de dimensões da matriz
    '''
    n, m = matrix.shape  # n = 3 m = 4

    '''
    print(f'\n{n} Linhas \n{m - 1} Colunas \n')
    print('-=' * 60)
    '''

    # Iniciando fase de eliminação!
    for i in range(0, n):  # Linha
        for j in range(i + 1, n):
            if matrix[j, i] != 0.0:  # matrix[j, i]

                print(
                    f'\nUsando a Linha {i + 1} como Pivô, triangular inferior passada: {i + 1}!\n')

                # Multiplicador PIVO
                multiplier = matrix[j, i] / matrix[i, i]
                # print(f'DEBUG: {multiplier}')
                # print(f'DEBUG: {matrix[i, j]}, {matrix[j, j]}, {multiplier}')
                # Apenas para detalhar o processo multiplicador
                matrix[j, i: m] = matrix[j, i: m] - \
                    multiplier * matrix[i, i: m]

                # print(f'\n{matrix}\n')
                # print('-=' * 60)
    # Iniciando fade se Substituição!
    x = []  # Guarda valor final
    substractor = 0.0
    for i in range(n - 1, -1, -1):  # linha
        # print(f'DEBUG: i: {i}') # Para debugar
        for j in range(0, n - i):  # Coluna
            # print(f'DEBUG: j: {j}') # Para debugar
            if j == 0:
                substractor = 0
            else:
                substractor = substractor + matrix[i, m - j - 1] * x[j - 1]
        x.append((matrix[i, m - 1] - substractor) / matrix[i, i])
        # print(f'DEBUG: x: {x}')
    return x
