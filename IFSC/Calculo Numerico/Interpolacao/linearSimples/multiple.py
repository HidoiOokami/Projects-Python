import numpy as np

data = np.array([
    [180, 175, 183, 168, 176, 165, 168, 183, 185],  # altura  => xi
    [77,  75,  74,  62,  88,  75,  50,  66,  74],  # peso    => yi
    [31,  22,  22,  20,  22,  28,  22,  19,  24],  # idade   => x2
    [1.5, 1.4, 1,  0.9, 1.1, 0.95, 0.9, 1.2, 2]  # comida(kg) => x3
])

# Retornara um tupla com tamanho totala == a 2 list
# tabém irá retornar o tamanho de cada uma dessas list nesse caso == 4
position, lenght = data.shape

# 1º Somatorias
xi = data[0]
yi = data[1]
x2i = data[2]
y2i = data[3]

# Lambda para retornar somatoria de xi * yi


def _xi_yi(xi, yi): return sum(xi*yi)

# Lambda para retornar somatoria de xi e yi


def _xi(xi): return sum(xi)


def _x2i(x2i): return sum(x2i)


def _yi(yi): return sum(yi)


def _y2i(y2i): return sum(y2i)

# Lambda para retornar somatoria de xi²


def _xi2(xi): return sum(xi**2)


print(f'DEBUG: {_y2i(y2i)}')


def B1(): return (lenght * _xi_yi(xi, yi) - _xi(xi) *
                  _yi(yi)) / (lenght * _xi2(xi) - ((_xi(xi))**2))


def B0(): return (_yi(yi) - _xi(xi) * B1()) / lenght


def y_chapeu(data): return B0() + B1() * data

# print(f'{y_chapeu(176)}')
