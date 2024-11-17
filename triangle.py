import math


def area(a, b, c):

    if not all(isinstance(i, (int, float)) for i in [a, b, c]):
        raise TypeError("All sides must be integers or floats")

    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("All sides must be positive")
    if not (a + b > c and a + c > b and b + c > a):
        raise ValueError("Impossible sides of the triangle")
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


def perimeter(a, b, c):

    if not all(isinstance(i, (int, float)) for i in [a, b, c]):
        raise TypeError("All sides must be integers or floats")

    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("All sides must be positive")
    if not (a + b > c and a + c > b and b + c > a):
        raise ValueError("Impossible sides of the triangle")
    return a + b + c
