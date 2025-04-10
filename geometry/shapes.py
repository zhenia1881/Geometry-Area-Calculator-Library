import math
from abc import ABC, abstractmethod
from dataclasses import dataclass


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def is_right_angled(self) -> bool:
        pass


@dataclass
class Circle(Shape):
    radius: float

    def __post_init__(self):
        if self.radius <= 0:
            raise ValueError("Radius must be positive")

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def is_right_angled(self) -> bool:
        return False


@dataclass
class Triangle(Shape):
    a: float
    b: float
    c: float

    def __post_init__(self):
        sides = sorted([self.a, self.b, self.c])
        if any(side <= 0 for side in sides):
            raise ValueError("All sides must be positive")
        if sides[0] + sides[1] <= sides[2]:
            raise ValueError("Invalid triangle sides")
        self.a, self.b, self.c = sides

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_angled(self, tolerance: float = 1e-6) -> bool:
        return abs(self.a ** 2 + self.b ** 2 - self.c ** 2) < tolerance