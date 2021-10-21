import math
import unittest
from unittest.mock import patch

from bnb.matrix_generator import MatrixGenerator


class TestMatrixGenerator(unittest.TestCase):
    def test_init_generator(self):
        matrix = MatrixGenerator(n_jobs=5)
        self.assertEqual(matrix.size()[0], 5)
        self.assertEqual(matrix.size()[1], 5)

    def test_is_diagonal_inf(self):
        matrix = MatrixGenerator(n_jobs=5)
        for i in range(5):
            self.assertTrue(math.isinf(matrix.get_element(i, i)))

    def test_is_ut1_lt30(self):
        matrix = MatrixGenerator(n_jobs=5)
        for i in range(5):
            for j in range(5):
                if i != j:
                    self.assertTrue(1 <= matrix.get_element(i, j) <= 30)

    def test_min(self):
        matrix = MatrixGenerator(n_jobs=5)
        self.assertEqual(min(matrix.pick_row(0)), matrix.min(0, 0))
        self.assertEqual(min(matrix.pick_col(0)), matrix.min(0, 1))

    def test_row_reduce(self):
        matrix = MatrixGenerator(n_jobs=5)
        min_idx = []
        for i in range(5):
            min_idx.append(matrix.pick_row(i).index(min(matrix.pick_row(i))))
        matrix._row_reduce()
        for i in range(5):
            self.assertEqual(min_idx[i], matrix.pick_row(i).index(0))

    def test_col_reduce(self):
        matrix = MatrixGenerator(n_jobs=5)
        min_idx = []
        for j in range(5):
            min_idx.append(matrix.pick_col(j).index(min(matrix.pick_col(j))))
        matrix._col_reduce()
        for j in range(5):
            self.assertEqual(min_idx[j], matrix.pick_col(j).index(0))

    def test_reduce_and_lower_bound(self):
        matrix = MatrixGenerator(n_jobs=5)
        min_val = []
        for i in range(5):
            min_val.append(min(matrix.pick_row(i)))
        matrix._row_reduce()
        for j in range(5):
            print(min(matrix.pick_col(j)))
            min_val.append(min(matrix.pick_col(j)))
        matrix._col_reduce()

        self.assertEqual(sum(min_val), matrix.lower_bound)

    def test_find_zero(self):
        matrix = MatrixGenerator(n_jobs=5)
        matrix._reduce()
        for idx in matrix._find_zero():
            self.assertEqual(0, matrix.get_element(idx[0], idx[1]))
