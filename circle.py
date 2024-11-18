import math


def area(r):
    if not isinstance(r, (int, float)):
        raise TypeError("The radius must be integers or floats")
    if r <= 0:
        raise ValueError("The radius must be positive")
    return math.pi * r * r


def perimeter(r):
    if not isinstance(r, (int, float)):
        raise TypeError("The radius must be integers or floats")
    if r <= 0:
        raise ValueError("The radius must be positive")
    return 2 * math.pi * r
