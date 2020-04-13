import Cholesky as cho
import numpy as np
from pprint import pprint


matrix = np.array([
    [16, -4, 12, -4],
    [-4,  2, -1,  1],
    [12, -1, 14, -2],
    [-4,  1, -2, 83]
])

result = cho.cholesky(matrix)
print()
# print(f'\nO resultade é: \n\nCUIDADO ORDEM INVERSA DE BAIXO PARA CIMA: \nXn -> ... -> X3 -> X2 -> X1')
# data = [result[_ :: -1] for _ in range(len(result))]

# print(str(result[:]).strip(''), end=' \n\n')
# Não a necessidade te fazer todas as converções

# TEMOS QUE TROCAR LINHA POR COLUNA NESSE CASO
# LINHA == COLUNA
# COLUNA == LINHA
print(f'CUIDADO COLUNA == LINHA e LINHA == COLUNA \n')

pprint(result)
print()
print('-=' * 60)
