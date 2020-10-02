from math import log10, sin, e
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


def get_min(f, left, right, eps):
    x_min = left
    y_min = f(left)
    i = left
    while i < right:
        if f(i) < y_min:
            x_min = i
            y_min = f(i)
        i += eps
    return x_min, y_min


def draw_function(X, Y, x_name, y_name, color='r'):
    plt.plot(X, Y, color)
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.show()


def build_function(function, X, y_name='y', color='r'):
    Y = []
    for x in X:
        Y.append(function(x))
    draw_function(X, Y, 'x', y_name, color)


def build_functions():
    build_function(f1, [0.01 * x for x in range(-50, 50)], '1', 'b')
    build_function(f2, [0.01 * x for x in range(600, 990)], '2', 'g')
    build_function(f3, [0.01 * x for x in range(0, 628)], '3', 'r')
    build_function(f4, [0.01 * x for x in range(0, 100)], '4', 'c')
    build_function(f5, [0.01 * x for x in range(50, 250)], '5', 'm')


def dichotomy_method(f, a, b, eps):
    delta = 0.49 * eps
    while b - a > eps:
        x1 = (a + b) / 2 - delta
        x2 = (a + b) / 2 + delta
        if f(x1) < f(x2):
            b = x2
        elif f(x1) > f(x2):
            a = x1
        else:
            a, b = x1, x2
    return a, f(a)


def find_all_min():
    functions = [
        [f1, -0.5, 0.5, 0.01],
        [f2, 6, 9.9, 0.01],
        [f3, 0, 6.28, 0.01],
        [f4, 0, 1, 0.01],
        [f5, 0.5, 2.5, 0.01]
    ]
    methods = [dichotomy_method]
    for row in functions:
        print("Function: " + str(row[0].__name__))
        for method in methods:
            method_result = method(row[0], row[1], row[2], row[3])
            real_result = get_min(row[0], row[1], row[2], row[3])
            print(method.__name__ + " result: " + str(method_result))
            print("Real result: " + str(real_result))
        print("================")

find_all_min()