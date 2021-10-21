import math
from random import randint


class InvalidAxisError(Exception):
    def __str__(self):
        return "잘못된 axis 입력"


class MatrixGenerator:
    def __init__(self, n_jobs: int = 10):
        self.n_jobs: int = n_jobs
        self.matrix = self._init_matrix()
        self.lower_bound = 0
        self.row_names = [i + 1 for i in range(n_jobs)]
        self.col_names = [j + 1 for j in range(n_jobs)]

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
        """return [row length, column length]"""
        return [len(self.matrix), len(self.matrix[0])]

    def show(self):
        print("  ", end="  ")
        for col_name in self.col_names:
            print(col_name, end="   ")
        print()
        for i in range(len(self.matrix)):
            print(self.row_names[i], self.matrix[i])

    def _reduce(self):
        self._row_reduce()
        self._col_reduce()

    def _row_reduce(self):
        for i in range(self.size()[0]):
            i_row_min = self.min(i, 0)
            self._accmulate_in_lower_bound(i_row_min)

            self.matrix[i] = [x - i_row_min for x in self.matrix[i]]

    def _col_reduce(self):
        for j in range(self.size()[1]):
            j_col_min = self.min(j, 1)
            self._accmulate_in_lower_bound(j_col_min)

            for i in range(self.size()[0]):
                self.matrix[i][j] -= j_col_min

    def _accmulate_in_lower_bound(self, time: int):
        self.lower_bound += time

    def min(self, i, axis):
        """
        get min value of i-th row(or column)
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

    def _find_zero(self):
        zero_list = []
        for i in range(self.size()[0]):
            for j in range(self.size()[1]):
                if self.get_element(i, j) == 0:
    def _delete_row(self, i):
        del self.matrix[i]
        self._update_name(i, 0)

    def _delete_col(self, j):
        for row in self.matrix:
            del row[j]
        self._update_name(j, 1)

    def _update_name(self, i, axis=0):
        """
        update name of i-th row(or column) after deleting row(or column)
        axis=0: row
        axis=1: column
        """
        if axis != 0 and axis != 1:
            raise InvalidAxisError()

        if axis == 0:
            del self.row_names[i]
            return

        del self.col_names[i]
        return
