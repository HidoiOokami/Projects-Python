import numpy as np


class SimpleLinearFitting:

    def __init__(self, x, y):
        self.x = np.array(x, dtype='float64')
        self.y = np.array(y, dtype='float64')
        self.solve()

    def solve(self):
        n = len(self.x)
        sumXiYi = np.sum(self.x) * np.sum(self.y)
        sumXi = np.sum(self.x)
        sumYi = np.sum(self.y)
        sumXiSquare = np.sum(self.x ** 2)
        self.beta_one = ((n * sumXiYi) - (sumXi * sumYi)) / \
            ((n * sumXiSquare) - (sumXi ** 2))
        self.beta_two = (sumYi - (sumXi * self.beta_one))/n

    def fit(self):
        return self.beta_one + self.beta_two * x
