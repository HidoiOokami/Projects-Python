import numpy as np

data = np.array([
    [-5, -4, -2, 0, 1, 2, 3, 5],  # altura => xi
    [368, 255, 54, 6, 13, 40, 110, 220]  # peso   => yi
])

# Garantindo que os dados de dada matriz sejam Flutuantes
data = data.astype(float)

# Retornara um tupla com tamanho totala == a 2 list
# tabém irá retornar o tamanho de cada uma dessas list nesse caso == 4
position, lenght = data.shape

# 1º Somatorias INVERTE DEPENDE DA QUESTÃO
xi = data[0]
yi = data[1]
f = 80  # Dado a ser passado

# Lambda para retornar somatoria de xi * yi


def _xi_yi(xi, yi):
    return sum(xi * yi)


# Lambda para retornar somatoria de xi e yi


def _xi(xi):
    return sum(xi)


def _yi(yi):
    return sum(yi)


# Lambda para retornar somatoria de xi²


def _xi2(xi, exp=2):
    return sum(xi**exp)


def _yi2(yi):
    return sum(yi**2)


def B1():
    return (lenght * _xi_yi(xi, yi) - _xi(xi) * _yi(yi)) / (lenght * _xi2(xi) -
                                                            ((_xi(xi))**2))


def B0():
    return (_yi(yi) - _xi(xi) * B1()) / lenght


def y_chapeu(data):
    return B0() + B1() * data


def desvio(x=xi):

    result = 0
    for _ in x:
        result += y_chapeu(_)
    return result


def coef_determination():
    sup = (_xi_yi(xi, yi) - (_xi(xi) * (_yi(yi) / lenght)))**2

    inf = ((_xi2(xi) - ((_xi(xi)**2) / lenght)) * (_yi2(yi) -
                                                   ((_yi(yi)**2) / lenght)))

    return sup / inf


print(
    f'\n\nDEBUG: \nTamanho = {lenght} \nYi * Xi = {_xi_yi(xi, yi)} \nYi = {_yi(yi)} \nXi = {_xi(xi)} \nXi² = {_xi2(xi)} \nB1 = {B1()} \nB0 = {B0()}\n\n'
)

print(f'Y^ = {y_chapeu(f)}')
print(f'D = {desvio()}')
print(f'Coeficiente de Determinação entre 0 e 1 = {coef_determination()}\n\n')
