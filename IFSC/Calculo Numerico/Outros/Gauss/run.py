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

import Gauss as gss
import numpy as np

matrix = np.array([
    [2,  3, -1,  5],
    [4,  4, -3,  3],
    [2, -3,  1, -1]
])
result = gss.gauss(matrix)

print(f'\nO resultade é: \n\nX1 -> X2 -> ... Xn')
# List Comprehension para imprimir bunitinhu :)
data = [result[_ :: -1] for _ in range(len(result))]


print(str(data[2]).strip('[]'), end=' \n\n')
# Não a necessidade te fazer todas as converções
# print(f'CUIDADO ORDEM INVERSA: \nXn -> ... -> X3 -> X2 -> X1 \n{result}')
print('-=' * 60)