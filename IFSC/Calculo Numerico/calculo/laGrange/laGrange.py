import numpy as np
import functools

result = 0
const = 80
data = np.array([(0, 0.0), (8.0, 10), (27.0, 30), (58.0, 60), (100, 90),
                 (145, 120), (160, 140)])

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
                    ret.append(
                        (x - samples[j][X]) / (samples[i][X] - samples[j][X]))
            return functools.reduce(lambda a, b: a * b, ret)

        return L_gen

    return lambda x: sum(L(i)(x) * samples[i][Y] for i in range(n))


# main passando minha lista de tuplas para o metodo
result = lagrangian_interpolate(data)

print(f'\nP3({const}): {result(const)}\n')
