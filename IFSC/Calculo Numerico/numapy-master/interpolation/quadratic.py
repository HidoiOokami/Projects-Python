import numpy as np


class QuadraticInterpolation:

    def __init__(self, points):
        self.points = points
        self.nPoints = len(points)
        self.solve()

    def solve(self):
        # step 1
        A = [[self.points[i][0] ** 2, self.points[i][0], 1]
             for i in range(self.nPoints)]
        A = np.array(A, dtype='float64')
        # step 2
        b = [self.points[i][1] for i in range(self.nPoints)]
        b = np.array(b, dtype='float64')
        # step 3
        results = np.linalg.solve(A, b)
        self.results = results

    def P(self, x):
        if self.results is None:
            raise ArithmeticError(
                'The result of points interpolation has not been calculated. ',
                'Please use solve before call the P method.')
        return self.results[0] * x ** 2 + self.results[1] * x + self.results[2]

    def getP(self):
        if self.results is None:
            raise ArithmeticError(
                'The result of points interpolation has not been calculated. ',
                'Please use solve before call the getP method.')
        return '{} * x ** 2 + {} * 2 + {}'.format(self.results[0], self.results[1], self.results[2])
