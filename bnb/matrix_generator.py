import math
from random import randint


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
