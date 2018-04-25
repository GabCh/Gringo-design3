import math
from typing import Tuple

from atlas.infrastructure.stream import Stream


class OrthogonalProjectionCalculator(object):

    def project(self, u: Tuple[float, ...], v: Tuple[float, ...]) -> Tuple[float, ...]:
        constant = self.dot_product(u, v) / (self.length(v) ** 2)
        return self.scalar_with_vector_product(constant, v)

    def dot_product(self, u: Tuple[float, ...], v: Tuple[float, ...]) -> float:
        return sum(Stream(zip(u, v)).map(lambda x, y: x * y))

    def length(self, u: Tuple[float, ...]) -> float:
        return math.sqrt(sum(Stream(u).map(lambda x: x ** 2)))

    def scalar_with_vector_product(self, number: float, vector: Tuple[float, ...]) -> Tuple[float, ...]:
        return tuple(Stream(vector).map(lambda x: x * number).toList())
