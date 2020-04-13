import numpy as np
import math
# as A matrix, Solution and B matrix


def seidel(a, x, b):
    # a = 3
    n = len(a)

    for j in range(0, n):
     
        d = b[j]

        for i in range(0, n):
            if(j != i):
                d -= (a[j][i] * x[i])
      
        x[j] = d / a[j][j]

    return x

precision = math.pow(10, -2)

x = [0, 0, 0]
a =  np.array([
    [5, 1, 1],
    [3, 4, 1],
    [3, 3, 6]
])
b = [5, 6, 0]


print(f'X = {x}\n\n')

for i in range(0, 25):
    x = seidel(a, x, b)
    # print each time the updated solution
    print(f'{i + 1}: RESULT = {x} \n')

