'''

          - Formula -
  Regra do Trapezio Composta

  ITc = h/2 * [fx(0) + 2 * f(1) + ... + f(xn)]

'''
import math
# Intervalo maior e menor
a = -2.
_a = a
b = 2.

# Numero de intervalos
n = 10.0
h = 0.0
cont = 0.0
summation, result = .0, .0

# Variação fatiamento
variation = lambda b, a, n: ((b) - (a)) / n


#def variation(b=b, a=a, n=n): return (b - a) / n


# Fx sempre mudara dependendo da integral que for passada
def fx(x): return math.e**(-(x**2)/2)


h = variation(b,a,n) / 2


while cont < (n - 1):
    #  variation() possui parametro opciona
    _a += variation(b,a,n)
    summation += 2.0 * fx(_a)
    print(f'DEBUG: fx({_a}) = {summation}')
    cont += 1

result = h * (fx(a) + summation + fx(b))


print(f'\nResultado: {h} * {(fx(a) + summation + fx(b))} = {result}')
