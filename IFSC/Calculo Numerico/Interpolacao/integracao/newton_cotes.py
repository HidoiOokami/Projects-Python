'''

          - Formula -
  Regra do Trapezio Composta

  ITc = h/2 * [fx(0) + 2 * f(1) + ... + f(xn)]

'''
# Intervalo maior e menor
a = 3.0
_a = a
b = 3.6

# Numero de intervalos
n = 6.0
h = 0.0
cont = 0.0
summation, result = .0, .0

# Variação fatiamento
# variation = lambda b, a, n: (b - a) / n


def variation(b=b, a=a, n=n): return (b - a) / n


# Fx sempre mudara dependendo da integral que for passada
def fx(x): return 1 / x


h = (variation() / 2)

# print(f'DEBUG: \n{type(variation())}')
while cont < (n - 1):
    #  variation() possui parametro opciona
    _a += variation()
    summation += 2.0 * fx(_a)
    print(f'DEBUG: fx({_a}) = {summation}')
    cont += 1

result = h * (fx(a) + summation + fx(b))


print(f'\nResultado: {h} * {(fx(a) + summation + fx(b))} = {result}')
