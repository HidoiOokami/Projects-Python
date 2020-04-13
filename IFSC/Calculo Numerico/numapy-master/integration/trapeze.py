import numpy as np


class Trapeze:

    def __init__(self, func, t, n, a, b):
        self.a = a
        self.b = b
        self.n = n
        self.t = t
        self.h = (b-a)/n
        self.f = func
        self.solve()

    def solve(self):
        if self.t == 'compost':
            self._solveCompost()
            return

    def _solveCompost(self):
        som = self.f(self.a) + self.f(self.b)
        sum_h = self.h + self.a
        for i in range(self.n - 1):
            som += 2 * self.f(sum_h)
            sum_h += self.h

        res = self.h/2 * som
        print('A integração usando o método do trapézio é: {}'.format(res))

    def error(self, func):
        x = []
        fsd_x = []

        i = 0
        while i <= self.n:
            x.append(self.a + i * self.h)
            fsd_x.append(func(x[i]))
            i += 1

        err = ((self.b - self.a) / 12) * self.h**2 * abs(max(fsd_x, key=abs))
        print('O erro máximo da integração usando Trapézio é: {}'.format(err))
