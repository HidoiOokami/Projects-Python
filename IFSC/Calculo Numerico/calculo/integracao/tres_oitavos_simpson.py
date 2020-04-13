import numpy as np

# Intervalo maior e menor
a = 0.0
b = 2.0
# Numero de intervalos
n = 12

if n % 3 == 0:
    print(f'N = {n} e multiplo de 3')
else:
    print(
        f'N = {n} não e multiplo de 3\nOpções [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33]'
    )
    exit(0)


def h(b=b, a=a, n=n):
    return (b - a) / n


# Fx sempre mudara dependendo da integral que for passada


def fx(x):
    return x**5  # np.log((x)**3 + np.sqrt(math.e**x + 1))


tres_oitavos = (3 * h()) / 8  # Variação aqui e por 3

summation = fx(a) + fx(b)

# print(f'DEBUG: \n{type(h())}')
for i in range(n):
    if i % 3 == 0:  # passando n se for multiplo de 3 passa 2
        summation += 2 * fx(a + i * h())
    else:
        summation += 3 * fx(a + i * h())

result = tres_oitavos * summation

print(f'\nResultado: {result}')
