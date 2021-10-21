import math
from random import randint


class InvalidAxisError(Exception):
    def __str__(self):
        return "잘못된 axis 입력"


class JobTable:
    def __init__(self, n_jobs: int = 10):
        self.n_jobs: int = n_jobs
        self.matrix = self._init_matrix()
        self.row_labels = [i + 1 for i in range(n_jobs)]
        self.col_labels = [j + 1 for j in range(n_jobs)]
        self.lower_bound = 0
        self.path_list = []

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
        for col_label in self.col_labels:
            print(col_label, end="   ")
        print()
        for i in range(len(self.matrix)):
            print(self.row_labels[i], self.matrix[i])

    def step_select_max_regret(self):
        self._reduce()
        self._select_max_regret()

    def _select_max_regret(self):
        if self.size()[0] == 1:
            return
        max_regret_i, max_regret_j = self._get_idx_max_regret()
        self._append_max_regret_path(max_regret_i, max_regret_j)
        self._make_reverse_path_impossible(max_regret_i, max_regret_j)
        self._delete_row(max_regret_i)
        self._delete_col(max_regret_j)

    def _append_max_regret_path(self, i, j):
        row_label = self.row_labels[i]
        col_label = self.col_labels[j]
        self.path_list.append([row_label, col_label])

    def _get_idx_max_regret(self):
        max_ = 0
        zero_idx_list = self._find_zero()
        idx = [zero_idx_list[0][0], zero_idx_list[0][1]]
        for i, j in zero_idx_list:
            regret_i_j = self._cal_regret(i, j)
            if regret_i_j > max_:
                max_ = regret_i_j
                idx = [i, j]

        return idx

    def _find_zero(self):
        zero_idx_list = []
        for i in range(self.size()[0]):
            for j in range(self.size()[1]):
                if self.get_element(i, j) == 0:
                    zero_idx_list.append([i, j])
        return zero_idx_list

    def _cal_regret(self, i, j):
        row = self.pick_row(i)
        row_without_j = row[:j] + row[j + 1 :]
        col = self.pick_col(j)
        col_without_i = col[:i] + col[i + 1 :]
        return min(row_without_j) + min(col_without_i)

    def _delete_row(self, i):
        del self.matrix[i]
        self._update_label(i, 0)

    def _delete_col(self, j):
        for row in self.matrix:
            del row[j]
        self._update_label(j, 1)

    def _update_label(self, i, axis=0):
        """
        update label of i-th row(or column) after deleting row(or column)
        axis=0: row
        axis=1: column
        """
        if axis != 0 and axis != 1:
            raise InvalidAxisError()

        if axis == 0:
            del self.row_labels[i]
            return

        del self.col_labels[i]
        return

    def _make_reverse_path_impossible(self, i, j):
        row_label = self.row_labels[i]
        col_label = self.col_labels[j]

        try:
            row_idx_equal_to_col_label = self.row_labels.index(col_label)
            col_idx_equal_to_row_label = self.col_labels.index(row_label)
            self.matrix[row_idx_equal_to_col_label][
                col_idx_equal_to_row_label
            ] = math.inf
        finally:
            return

    def step_not_select_max_regret(self):
        self._not_select_max_regret()
        self._reduce()

    def _not_select_max_regret(self):
        self._reduce()
        self._make_unselected_path_impossible()
        self._reduce()

    def _make_unselected_path_impossible(self):
        max_regret_i, max_regret_j = self._get_idx_max_regret()
        self.matrix[max_regret_i][max_regret_j] = math.inf

    def _reduce(self):
        self._row_reduce()
        self._col_reduce()

    def _row_reduce(self):
        for i in range(self.size()[0]):
            i_row_min = self.min(i, 0)
            self._accmulate_in_lower_bound(i_row_min)

            if math.isinf(i_row_min):
                self.lower_bound = math.inf

            self.matrix[i] = [x - i_row_min for x in self.matrix[i]]

    def _col_reduce(self):
        for j in range(self.size()[1]):
            j_col_min = self.min(j, 1)
            self._accmulate_in_lower_bound(j_col_min)

            if math.isinf(j_col_min):
                self.lower_bound = math.inf

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
        return self.matrix[i][:]

    def pick_col(self, j):
        return [row[j] for row in self.matrix]
