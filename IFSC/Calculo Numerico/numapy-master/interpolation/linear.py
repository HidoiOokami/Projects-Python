import numpy as np


class LinearInterpolation:
    """ Class for solve Linear Interpolation problems.

    Author: Medeiros Gilberto

    Version: 0.1.0
    """

    def __init__(self, points):
        """
        Keyword Arguments:
        - points - tuple of points that will be used for interpolation.
        """
        self.points = points
        self.nPoints = len(self.points)
        self.solve()  # Call the solve method for calculate the beta scalars.

    def solve(self) -> list:
        """ Solve the linear system using numpy linalg solve method and
        returns the scalars to `self.result` attr used for P and getP methods.
        """
        # step 1
        A = [[1 * self.points[i][0], 1] for i in range(self.nPoints)]
        A = np.array(A, dtype='float64')
        # step 2
        b = [self.points[i][1] for i in range(self.nPoints)]
        b = np.array(b, dtype='float64')
        # step 3
        results = np.linalg.solve(A, b)
        self.results = results

    def P(self, x) -> float:
        """Return the P function, or interpolated function, evaluated
        at x.

        Keyword arguments:
        - x - Point that will be used to evaluate the interpolation function.
        """
        if self.results is None:
            raise ArithmeticError(
                'The result of points interpolation has not been calculated. ',
                'Please use solve before call the P method.')
        return self.results[0] * x + self.results[1]

    def getP(self) -> str:
        """Return the P function in string format."""
        if self.results is None:
            raise ArithmeticError(
                'The result of points interpolation has not been calculated. ',
                'Please use solve before call the getP method.')
        return '{} * x + {}'.format(self.results[0], self.results[1])
