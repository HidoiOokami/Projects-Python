'''

          - Formula -
  Regra do 1/3 simpsom

  ITc = h/2 * [fx(0) + 2 * f(1) + ... + f(xn)]

'''

import numpy as np
from scipy import integrate

# Intervalo maior e menor
a = np.pi / 2  # valor de baixo
_a = a
b = np.pi  # valor de cima

# Numero de intervalos
n = 10  # tem que ser par
h = 0.0
cont = 0.0
summation, result = .0, .0

# Variação fatiamento
# variation = lambda b, a, n: (b - a) / n


def variation(b=b, a=a, n=n):
    return (b - a) / n


# Fx sempre mudara dependendo da integral que for passada
def fx(x):
    return np.sin(x)


h = (variation() / 3)  # Variação aqui e por 3

# print(f'DEBUG: \n{type(variation())}')
while cont < (n - 1):
    #  variation() possui parametro opciona
    _a += variation()
    if cont % 2 == 0:
        summation += 4.0 * fx(_a)
    elif cont % 2 == 1:
        summation += 2.0 * fx(_a)
    print(f'DEBUG: fx({_a}) = {summation}')
    cont += 1

result = h * (fx(a) + summation + fx(b))

print(f'\nResultado: {h} * {(fx(a) + summation + fx(b))} = {result}')
print(
    f'Valor exato: {integrate.quad(lambda x: -np.cos(x), (np.pi/2), np.pi)[0]}'
)

f_quad = lambda x: np.sin(x)
# 1° Parametro função original
# 2° Parametro valor de A
# 3° Parametro valor de B
# 4° Parametro expoente da função para integral de valor N
integral = integrate.fixed_quad(f_quad, (np.pi / 2), np.pi, n=4)
print(f'Integral de valor N: {integral}')
