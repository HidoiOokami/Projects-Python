import numpy as np


class SecondSimpsonIntegration:

    def __init__(self, func, k, a, b):
        self.k = k
        self.a = a
        self.b = b
        self.h = (b - a)/k
        self.f = func
        self.solve()

    def solve(self):

        res = self.f(self.a) + self.f(self.b)

        for i in range(1, self.k):
            if i % 3 == 0:
                res += 2 * self.f(self.a + i * self.h)
            else:
                res += 3 * self.f(self.a + i * self.h)

        res = ((3*self.h) / 8) * res
        print('O resultado da integração numérica é: {}'.format(res))

    def error(self, func):
        x = []
        fiv_x = []

        i = 0
        while i <= self.k:
            x.append(self.a + i * self.h)
            fiv_x.append(func(x[i]))
            i += 1

        err = ((self.b - self.a)/80) * self.h ** 4 * max(fiv_x)
        print('O erro máximo da integração usando 3/8 Simpson é: {}'.format(err))
