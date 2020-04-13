from math import sqrt

# Executa uma decomposição de Cholesky de A, que deve
# ser uma matriz definida simétrica e positiva. A função
# etorna a matriz triangular variante inferior, L.


def cholesky(A):

    n = len(A)

    # Criar a matriz zero para L
    L = [[0.0] * n for i in range(n)]

    # Realize a decomposição de Cholesky
    for i in range(n):
        for k in range(i + 1):
            # A função sum () adiciona o início e os itens do iterável especificado da esquerda para a direita.
            # EX:5 sum([1, 2, 3, 4, 5]) >> 15
            tmp_sum = sum(L[i][j] * L[k][j] for j in range(k))

            if (i == k):  # Elementos diagonais
                # LaTeX: l_{kk} = \sqrt{ a_{kk} - \sum^{k-1}_{j=1} l^2_{kj}}
                L[i][k] = sqrt(A[i][i] - tmp_sum)
            else:
                # LaTeX: l_{ik} = \frac{1}{l_{kk}} \left( a_{ik} - \sum^{k-1}_{j=1} l_{ij} l_{kj} \right)
                L[i][k] = (1.0 / L[k][k] * (A[i][k] - tmp_sum))
    return L
