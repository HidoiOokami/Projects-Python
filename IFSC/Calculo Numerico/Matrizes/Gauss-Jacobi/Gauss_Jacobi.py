# -*- coding: utf-8 -*-
"""
Criado por:
bed72 - Gabriel Ramos

"""
import numpy as np

# Retornando maior valor da matriz para criterio de convergencia


def convergence(matrix):
    max_elemnt = max([valor for linha in matrix for valor in linha])
    
    _max = matrix[0][0]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if abs(matrix[i][j]) > _max:
                _max = abs(matrix[i][j])
    return _max

# Metodo para retornar os ultimos elemento da matrix formando o vetor 'b'


def bk(matrix, lengt):
    # 'bk' são os elemento de 'b'
    bk = []

    # Pegando ultimos elemento
    for i in range(0, lengt):
        bk.append(matrix[i, -1])

    return bk


def gauss_jacobi(matrix, x0, precision):

    # Garantindo uma matriz, asarray converte a entrada em uma matriz
    np.asarray(matrix)
    # Garantindo que os dados de dada matriz sejam Flutuantes
    matrix = matrix.astype(float)

    n, m = matrix.shape  # n = 3 m = 4
    _bk = bk(matrix, n)
    # print(f'DEBUG: bk={_bk}\n\n')

    # Testando criterio de convergencia
    # 'np.zeros' Retorne uma nova matriz de determinada forma e tipo, preenchida com zeros.
    len_matrix = np.zeros((n, 1))
    # print(f'DEBUG: {len(len_matrix)}\n')
    for i in range(n):  # n == len(matrix)
        _sum = 0  # soma
        _list = list(range(n))
        # Agora eu quero que percorra todos os elemento da coluna exceto o próprio elemento
        _list.remove(i)
        # For para percorre nova list
        for j in _list:
            _sum += matrix[i][j]
        # 'matrix[i][i]' é a diagonal
        # diagonal da matrix passada
        len_matrix[i][0] = abs(_sum / matrix[i][i])

    print(f'A matriz atende ao critério!' if convergence(
        len_matrix) <= 1 else 'Não atende!')

    # Criando a matriz C de  Cx+G

    C = np.zeros((n, n))  # A matriz C  de Cx + G
    G = np.zeros((n, 1))  # o vetor coluna G de Cx + G
    x0 = np.zeros((n, 1))  # o vetor x de Ax=B
    # print(f'DEBUG: C={C}\nG={G}\n\n')

    for i in range(n):

        for j in range(n):
            if i == j:
                C[i][j] = 0
            else:
                # Se diagonal for diferente de 0
                if matrix[i][i] != 0:
                    C[i][j] = -matrix[i][j] / matrix[i][i]
                else:
                    print(f'Divisão por zero!')
                    break
        if matrix[i][i] != 0:
            # Colocando os valores de G _bk e o meu 'b' extraido da matrix
            G[i][0] = _bk[i] / matrix[i][i]
    # Realizando iterações
    count = 0

    while True:
        count += 1
        # print(f'DEBUG: C={C}\nx0=\n{x0}\nG=\n{G}\n')
        xk = np.dot(C, x0) + G
        # print(f'DEBUG: xk=\n{xk}\n\n')
        # result = np.array(convergence(xk-x0) / convergence(xk))
        result = convergence(xk-x0) / convergence(xk)
        print(f'DEBUG: result={result}\nprecision={precision}\n')
       
        if result < precision:
        #if count < 10:
            break
        else:
            x0 = xk

    # Imprimir solucao
    print(f'Solução: \n')
    for i in range(n):
        print(f'x{(i + 1)} = {xk[i][0]}')
    print(f'\nNumero de iterações = {count}')
