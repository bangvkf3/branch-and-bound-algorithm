import math
import unittest
from unittest.mock import patch

from bnb.matrix_generator import MatrixGenerator


class TestMatrixGenerator(unittest.TestCase):
    def test_init_generator(self):
        matrix = MatrixGenerator(n_jobs=5)
        self.assertEqual(matrix.size()[0], 5)
        self.assertEqual(matrix.size()[1], 5)
        matrix.show()

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
