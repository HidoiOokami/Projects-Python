import numpy as np

data = np.array([
    [-1, -0.5, 0, 0.4, 0.7, 1],  # altura => xi
    [2.05, 0.4, 0, 0.6, 1.2, 2.05]  # peso   => yi
])

x = data[0]
y = data[1]

polinomial = lambda x, y, const=2: np.polyfit(x, y, const)


# Função
# y = B0 + B1*x + B2*x²
def fx(vetor, const):
    # O vetor vira de tras para frente
    return vetor[-1] + (vetor[-2] * const) + (vetor[0] * (const**2))


data = polinomial(x, y)

print(f"Resultados: \n{data} \n{fx(data, -0.2)}")
