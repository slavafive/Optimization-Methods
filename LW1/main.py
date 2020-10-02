from math import log10, sin, e
import numpy
from matplotlib import pyplot as plt


def f1(x):
    return -5 * x ** 5 + 4 * x ** 4 - 12 * x ** 3 + 11 * x ** 2 - 2 * x + 1


def f2(x):
    return log10(x - 2) ** 2 + log10(10 - x) ** 2 - x ** 0.2


def f3(x):
    return -3 * x * sin(0.75 * x) + e ** (-2 * x)


def f4(x):
    return e ** (3 * x) + 5 * e ** (-2 * x)


def f5(x):
    return 0.2 * x * log10(x) + (x - 2.3) ** 2


def draw_function(X, Y, x_name, y_name, color='r'):
    plt.plot(X, Y, color)
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.show()


def build_function(function, X, color='r'):
    Y = []
    for x in X:
        Y.append(function(x))
    draw_function(X, Y, 'x', 'y', color)


def build_functions():
    build_function(f1, [0.01 * x for x in range(-50, 50)], 'b')
    build_function(f2, [0.01 * x for x in range(600, 990)], 'g')
    build_function(f3, [0.01 * x for x in range(0, 630)], 'r')
    build_function(f4, [0.01 * x for x in range(0, 100)], 'c')
    build_function(f5, [0.01 * x for x in range(50, 250)], 'm')


build_functions()
