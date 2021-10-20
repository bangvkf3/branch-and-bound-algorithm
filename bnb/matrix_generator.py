import math
from random import randint


class InvalidAxisError(Exception):
    def __str__(self):
        return "잘못된 axis 입력"


class MatrixGenerator:
    def __init__(self, n_jobs: int = 10):
        self.n_jobs: int = n_jobs
        self.matrix = self._init_matrix()

    def _init_matrix(self):
        matrix = [[0] * self.n_jobs for _ in range(self.n_jobs)]
        for i in range(self.n_jobs):
            for j in range(self.n_jobs):
                if i == j:
                    matrix[i][j] = math.inf
                else:
                    matrix[i][j] = randint(1, 30)

        return matrix

    def get_element(self, i, j):
        return self.matrix[i][j]

    def size(self):
        return [len(self.matrix), len(self.matrix[0])]

    def show(self):
        print(self.matrix)

    def _row_reduction(self):
        pass

    def _col_reduction(self):
        pass

    def min(self, i, axis):
        """get min value of i-th row(or column)
        axis=0: row
        axis=1: column
        """
        if axis != 0 and axis != 1:
            raise InvalidAxisError()

        if axis == 0:
            return min(self.pick_row(i))

        return min(self.pick_col(i))

    def pick_row(self, i):
        return self.matrix[i]

    def pick_col(self, j):
        return [row[j] for row in self.matrix]
