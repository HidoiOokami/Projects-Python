import numpy as np


class MultipleLinearFitting:

    def __init__(self, points):
        self.points = points
        self.numPoints = len(points)
        self.numDim = len(points[0])

    def solve(self):
        A = np.zeros((self.numDim, self.numDim), dtype='float64')
        A[0][0] = self.numPoints

        for i in range(1, self.numDim, 1):
            som = 0
            for k in range(0, self.numPoints, 1):
                som += self.points[k][i - 1]
            A[0][i] = som
            A[i][0] = som

        for i in range(1, self.numDim, 1):
            som = 0
            for k in range(0, self.numPoints, 1):
                som += self.points[k][i-1] ** 2
            A[i][i] = som

        pos = 2
        for i in range(1, self.numDim - 1, 1):
            j = pos
            while j < (self.numDim):
                som = 0
                for k in range(0, self.numPoints, 1):
                    som += self.points[k][i-1] * self.points[k][i]
                A[i][j] = som
                A[j][i] = som
                j += 1
            pos += 1

        vector_b = np.zeros(self.numDim)
        somY = 0
        for i in range(self.numPoints):
            somY += self.points[i][self.numDim-1]
        vector_b[0] = somY
        
        for i in range(1, self.numDim, 1):
            som = 0
            for k in range(self.numPoints):
                som += self.points[k][i-1] * self.points[k][self.numDim-1]
            vector_b[i] = som

        print(np.linalg.solve(A, vector_b))