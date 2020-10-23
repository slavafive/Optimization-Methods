def f1(x1, x2):
    return 100 * (x2 - x1 ** 2) ** 2 + (1 - x1) ** 2


def f2(x1, x2):
    return (x2 - x1 ** 2) ** 2 + (1 - x1) ** 2


def f3(x1, x2):
    return (1.5 - x1 * (1 - x2)) ** 2 + (2.25 - x1 * (1 - x2 ** 2)) ** 2 + (2.625 - x1 * (1 - x2 ** 3)) ** 2


def f4(x1, x2, x3, x4):
    return (x1 + x2) ** 2 + 5 * (x3 - x4) ** 2 + (x2 - 2 * x3) ** 4 + 10 * (x1 - x4) ** 4


def steepest_descent_method():
    pass


def coordinate_descent_method():
    pass


def brent_method():
    pass