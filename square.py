def area(a):
    if not isinstance(a, (int, float)):
        raise TypeError("The side must be integers or floats")
    if a <= 0:
        raise ValueError("The side must be positive")
    return a * a


def perimeter(a):
    if not isinstance(a, (int, float)):
        raise TypeError("The side must be integers or floats")
    if a <= 0:
        raise ValueError("The side must be positive")
    return 4 * a
