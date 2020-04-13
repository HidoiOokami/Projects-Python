from integration import Trapeze
from interpolation import LinearInterpolation
from interpolation import QuadraticInterpolation
from curvefitting import MultipleLinearFitting
import numpy as np
from scipy import integrate

# Test Linear Interpolation
# pontos = [(30, 3), (40, 5)]
# g = 37
# nPontos = 2

# linearIp = LinearInterpolation(pontos)
# print(linearIp.P(g))  # 4.4

# Test Quadratic Interpolation
# pontos = [(3, 20.08), (3.2, 24.53), (3.4, 29.96)]
# g = 3.1
# nPontos = 3
# quadIp = QuadraticInterpolation(pontos)
# print(quadIp.P(g))  # 22.18249999999999
# 12.250000000000622 * x ** 2 + -53.70000000000398 * 2 + 70.93000000000636
# print(quadIp.getP())

# x = [[2, 3, 6, 4, 6],
#      [2, 3, 6, 4, 6],
#      [2, 3, 6, 4, 6],
#      [2, 3, 6, 4, 6]]
# y = [2, 3, 6, 5, 3]

# mp = MultipleLinearFitting(x, y)
# mp.solve()


# AJUSTE LINEAR MULTIPLO
points = [
    (9,  87, 642),
    (14, 86, 464),
    (6,  78, 579),
    (11, 94, 550),
    (10, 77, 490),
    (8,  104, 710),
    (4,  80, 600)
]

ajusty = MultipleLinearFitting(points)
ajusty.solve()
# Formula Y = B0 + B1*X1 + B2*X2
# B2 -> B1 -> B0


def px(x, y):
    return 6.53663485*x - 19.2019243*y + 180.61694068


print(f'{px(80, 12)}')


# -------- TRAPÉZIO COMPOSTO --------


# Parametros:
# 1 - Função (lambda x: logica da funcao)
# 2 - Tipo de integração (usar somente 'compost')
# 3 - N (numero de divisões)
# 4 - A - limite inferior
# 5 - B - limite superior
# O resultado já é printado na tela

# DESCOMENTAR LINHA ABAIXO SE FOR UTILIZAR E MUDAR OS PARAMETROS
# -> trapeze = Trapeze(lambda x: np.sin(x), 'compost', 30, np.pi/2, np.pi)

# Para retornar o erro basta chamar a função error e passar como parâmetro
# a derivada segunda da função de integração

# DESCOMENTAR LINHA ABAIXO SE FOR UTILIZAR E MUDAR OS PARÂMETROS
# -> trapeze.error(lambda x: -np.sin(x))


# -------- 1/3 SIMPSON ---------

# Parametros:
# 1 - Função (lambda x: logica da funcao)
# 2 - N (numero de divisões)
# 3 - A - limite inferior
# 4 - B - limite superior
# O resultado já é printado na tela

# DESCOMENTAR LINHA ABAIXO SE FOR UTILIZAR E MUDAR OS PARAMETROS
# -> simpson = SimpsonIntegration(lambda x: np.sin(x), 10, np.pi/2, np.pi)

# Para retornar o erro basta chamar a função error e passar como parâmetro
# a derivada quarta da função de integração [Nesse caso a derivada
# era igual a função mas somente nesse caso pois é uma trigonométrica]

# DESCOMENTAR LINHA ABAIXO SE FOR UTILIZAR E MUDAR OS PARÂMETROS
# -> simpson.error(lambda x: np.sin(x))

# -------- 3/8 SIMPSON ---------

# Parametros:
# 1 - Função (lambda x: logica da funcao)
# 2 - N (numero de divisões)
# 3 - A - limite inferior
# 4 - B - limite superior
# O resultado já é printado na tela

# DESCOMENTAR LINHA ABAIXO SE FOR UTILIZAR E MUDAR OS PARAMETROS
# -> sndSimpson = SecondSimpsonIntegration(lambda x: np.sin(x), 12, np.pi/2, np.pi)

# Para retornar o erro basta chamar a função error e passar como parâmetro
# a derivada quarta da função de integração [Nesse caso a derivada
# era igual a função mas somente nesse caso pois é uma trigonométrica]

# DESCOMENTAR LINHA ABAIXO SE FOR UTILIZAR E MUDAR OS PARÂMETROS
# -> sndSimpson.error(lambda x: np.sin(x))
