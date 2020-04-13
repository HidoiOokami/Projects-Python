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
    [3841600, 1960, 1, 683908],
    [3880900, 1970, 1, 1235030],
    [3920400, 1980, 1, 1814950]
])



result = gss.gauss(matrix)

print(f'\nO resultade é: \n\nCUIDADO ORDEM INVERSA: \nXn -> ... -> X3 -> X2 -> X1')
# List Comprehension para imprimir bunitinhu :)
#data = [result[_:: -1] for _ in range(len(result))]

print(str(result).strip('[]'), end=' \n\n')
# Não a necessidade te fazer todas as converções
#print(f'CUIDADO ORDEM INVERSA: \nXn -> ... -> X3 -> X2 -> X1 \n{result}')
print('-=' * 60)
