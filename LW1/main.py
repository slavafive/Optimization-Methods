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
        else:
            a = x1
    return (a + b) / 2, f((a + b) / 2)


def golden_ratio_method(f, a, b, eps):
    golden_ratio = 0.5 * (3 - 5 ** 0.5)
    x1 = a + golden_ratio * (b - a)
    x2 = b - golden_ratio * (b - a)
    y1 = f(x1)
    y2 = f(x2)
    while b - a > eps:
        # print("a = ", a, "\tx1 =", x1, "\t x2 =", x2, "\tb = ", b)
        if y1 < y2:
            b = x2
            x2, y2 = x1, y1
            x1 = a + golden_ratio * (b - a)
            y1 = f(x1)
        else:
            a = x1
            x1, y1 = x2, y2
            x2 = b - golden_ratio * (b - a)
            y2 = f(x2)
    return (a + b) / 2, f((a + b) / 2)


def parabolic_minimum(x1, x2, x3, y1, y2, y3):
    return x2 - 0.5 * ((x2 - x1) ** 2 * (y2 - y3) - (x2 - x3) ** 2 * (y2 - y1)) / (
                (x2 - x1) * (y2 - y3) - (x2 - x3) * (y2 - y1))


def parabolic_interpolation_method(f, a, b, eps):
    x1, x2, x3 = a, (a + b) / 2, b
    y1, y2, y3 = f(x1), f(x2), f(x3)
    while x3 - x1 > eps:
        u = parabolic_minimum(x1, x2, x3, y1, y2, y3)
        yu = f(u)
        if u < x2:
            if yu < y2:
                x3, y3 = x2, y2
                x2, y2 = u, yu
            else:
                x1, y1 = u, yu
        else:
            if yu < y2:
                x1, y1 = x2, y2
                x2, y2 = u, yu
            else:
                x3, y3 = u, yu
    return (x1 + x3) / 2, f((x1 + x3) / 2)


def are_values_different(a, b, c):
    if a == b or a == c or b == c:
        return False
    return True


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0


def brent_method(f, a, c, eps):
    golden_ratio = 0.5 * (3 - 5 ** 0.5)
    x = w = v = (a + c) / 2
    yx = yw = yv = f(x)
    d = e = c - a
    while c - a > eps:
        g, e = e, d
        if are_values_different(x, w, v) and are_values_different(yx, yw, yv):
            u = parabolic_minimum(w, x, v, yw, yx, yv)
            if a + eps <= u <= c - eps and abs(u - x) < g / 2:
                d = abs(u - x)
        else:
            if x < (c - a) / 2:
                u = x + golden_ratio * (c - x)
                d = c - x
            else:
                u = x - golden_ratio * (x - a)
                d = x - a
        if abs(u - x) < eps:
            u = x + sign(u - x) * eps
        yu = f(u)
        if yu <= yx:
            if u >= x:
                a = x
            else:
                c = x
            v, w, x = w, x, u
            yv, yw, yx = yw, yx, yu
        else:
            if u >= x:
                c = u
            else:
                a = u
            if yu <= yw or w == x:
                v, w = w, u
                yv, yw = yw, yu
            elif yu <= yv or v == x or v == w:
                v, u = yv, yu


def find_all_min():
    functions = [
        [f1, -0.5, 0.5, 0.01],
        [f2, 6, 9.9, 0.01],
        [f3, 0, 6.28, 0.01],
        [f4, 0, 1, 0.01],
        [f5, 0.5, 2.5, 0.01]
    ]
    methods = [dichotomy_method, golden_ratio_method, parabolic_interpolation_method, brent_method]
    for row in functions:
        print("Function: " + str(row[0].__name__))
        for method in methods:
            method_result = method(row[0], row[1], row[2], row[3])
            print(method.__name__ + " result: " + str(method_result))
        real_result = get_min(row[0], row[1], row[2], row[3])
        print("real result: " + str(real_result))
        print("=======================================")


find_all_min()
