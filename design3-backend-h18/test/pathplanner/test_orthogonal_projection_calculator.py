import unittest

import math

from atlas.pathfinder.orthogonal_projection_calculator import OrthogonalProjectionCalculator


class OrthogonalProjectionCalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calculator = OrthogonalProjectionCalculator()

    def test_whenCalculatingDotProduct_thenMultiplyEachComponentIndividually(self):
        a_vector = (1, 1)
        a_second_vector = (2, 1)

        product = self.calculator.dot_product(a_vector, a_second_vector)

        self.assertEqual(3, product)

    def test_whenCalculatingVectorLength_thenReturnTheEuclideanDistance(self):
        a_vector = (1, 1)

        length = self.calculator.length(a_vector)

        self.assertEqual(math.sqrt(2), length)

    def test_whenMultiplyingScalarWithAVector_thenEachComponentIsMultipliedByTheConstant(self):
        a_vector = (1, 2, 3)
        a_constant = 5

        product = self.calculator.scalar_with_vector_product(a_constant, a_vector)

        self.assertEqual((5, 10, 15), product)
