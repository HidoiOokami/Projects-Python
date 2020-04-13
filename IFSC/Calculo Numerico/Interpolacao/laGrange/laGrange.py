import numpy as np
import functools

result = 0
const = 100
data = np.array([
    (86.0, 1.552),
    (93.3, 1.548),
    (98.9, 1.544),
    (104.4, 1.538),
    (110.0, 1.532)
])


# Metodo
def lagrangian_interpolate(samples):
    """
    Toma algumas amostras como uma lista de tuplas e retorna uma função que é
    uma interpolação lagrangiana de todas as amostras.
    """
    X = 0  # o índice de tupla da variável X nas amostras
    Y = 1  # o índice de tupla da variável Y nas amostras
    n = len(samples)
    # definir a função L como um gerador de funções que gera funções L
    # para um dado i
    print()

    def L(i):
        print("Está função gera uma função L para um determinado => x_i")

        def L_gen(x):
            ret = []
            for j in range(n):
                if j != i:
                    ret.append((x - samples[j][X]) /
                               (samples[i][X] - samples[j][X]))
            return functools.reduce(lambda a, b: a*b, ret)
        return L_gen

    return lambda x: sum(L(i)(x) * samples[i][Y] for i in range(n))


# main passando minha lista de tuplas para o metodo
result = lagrangian_interpolate(data)

print(f'\nP3({const}): {result(const)}\n')
