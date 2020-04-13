import numpy as np

data = np.array([
    [180, 175, 183, 168, 176, 165, 168, 183, 185], # altura => xi
    [77,  75,  74,  62,  88,  75,  50,  66,  74]   # peso   => yi
])

# Retornara um tupla com tamanho totala == a 2 list 
# tabém irá retornar o tamanho de cada uma dessas list nesse caso == 4
position, lenght = data.shape

# 1º Somatorias 
xi = data[0]
yi = data[1]

# Lambda para retornar somatoria de xi * yi
_xi_yi = lambda xi, yi: sum(xi*yi)

# Lambda para retornar somatoria de xi e yi
_xi = lambda xi: sum(xi)

_yi = lambda yi: sum(yi)

# Lambda para retornar somatoria de xi²
_xi2 = lambda xi: sum(xi**2)


def B1(): return (lenght * _xi_yi(xi, yi) - _xi(xi) * _yi(yi)) / (lenght * _xi2(xi) - ((_xi(xi))**2))

def B0(): return (_yi(yi) - _xi(xi) * B1()) / lenght

def y_chapeu(data): return B0() + B1() * data 

print(f'{y_chapeu(176)}')