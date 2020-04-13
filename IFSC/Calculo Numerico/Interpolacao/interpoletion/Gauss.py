import numpy as np


# Interpolação linear
def interpolation_linear(vector, data=0):
    print(f'\nInterpolação Linear\n')
    calculate = vector[0] * data + vector[1]
    print(f'P2({data}) = {calculate}\n')
    print('-=' * 60)


def interpolation_quadratic(vector, data=0):
    print(f'\nInterpolação Linear Quadratica\n')

    #calculate = vector[2] * (data**2) + vector[1] * data + vector[0]
    calculate = vector[0] * (data**2) + vector[1] * data + vector[2]
    print(f'P3({data}) = {calculate}\n')
    print('-=' * 60)


def gauss_interpolation(matrix, vector_B):
    result = np.linalg.solve(matrix, vector_B)
    # Resultado final
    print(f'\nGAUSS: \nOs valores de Xn: \n')
    for count, x in enumerate(result):
        print(f'X{(count + 1)} = {x}')
    print()
    print('-=' * 60)

    interpolation_quadratic(result, 3.1)
    #interpolation_linear(result, 50)
