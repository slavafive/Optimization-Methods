import numpy as np
import random
from matplotlib import pyplot as plt


def f1(x1, x2):
    return 100 * (x2 - x1 ** 2) ** 2 + (1 - x1) ** 2


def f1_derivative_x1(x1, x2):
    return -400 * x1 * x2 + 400 * x1 ** 3 + 2 * x1 - 2


def f1_derivative_x2(x1, x2):
    return 200 * (x2 - x1 ** 2)


def f2(x1, x2):
    return (x2 - x1 ** 2) ** 2 + (1 - x1) ** 2


def f2_derivative_x1(x1, x2):
    return 2 * (2 * x1 ** 3 - 2 * x1 * x2 + x1 - 1)


def f2_derivative_x2(x1, x2):
    return 2 * (x2 - x1 ** 2)


def f3(x1, x2):
    return (1.5 - x1 * (1 - x2)) ** 2 + (2.25 - x1 * (1 - x2 ** 2)) ** 2 + (2.625 - x1 * (1 - x2 ** 3)) ** 2


def f3_derivative_x1(x1, x2):
    return 2 * x1 * (x2 ** 6 + x2 ** 4 - 2 * x2 ** 3 - x2 ** 2 - 2 * x2 + 3) + 5.25 * x2 ** 3 + 4.5 * x2 ** 2 + 3 * x2 - 12.75


def f3_derivative_x2(x1, x2):
    return x1 * (x1 * (6 * x2 ** 5 + 4 * x2 ** 3 - 6 * x2 ** 2 - 2 * x2 - 2) + 15.75 * x2 ** 2 + 9 * x2 + 3)


def f4(x1, x2, x3, x4):
    return (x1 + x2) ** 2 + 5 * (x3 - x4) ** 2 + (x2 - 2 * x3) ** 4 + 10 * (x1 - x4) ** 4


def f4_derivative_x1(x1, x2, x3, x4):
    return 2 * (20 * (x1 - x4) ** 3 + x1 + x2)


def f4_derivative_x2(x1, x2, x3, x4):
    return 2 * (x1 + 2 * (x2 - 2 * x3) ** 3 + x2)


def f4_derivative_x3(x1, x2, x3, x4):
    return 10 * (x3 - x4) - 8 * (x2 - 2 * x3) ** 3


def f4_derivative_x4(x1, x2, x3, x4):
    return 10 * (-4 * (x1 - x4) ** 3 + x4 - x3)


def does_converge(a, b, eps):
    return np.linalg.norm(np.subtract(a, b)) < eps


def initialise_arguments(f):
    if f == f1:
        return np.array([-1.0, -1.0])
    elif f == f2:
        return np.array([-1.0, -1.0])
    elif f == f3:
        return np.array([-1.0, -1.0])
    elif f == f4:
        return np.array([-3.0, -3.0, -3.0, -3.0])


derivatives = {
    f1: [f1_derivative_x1, f1_derivative_x2],
    f2: [f2_derivative_x1, f2_derivative_x2],
    f3: [f3_derivative_x1, f3_derivative_x2],
    f4: [f4_derivative_x1, f4_derivative_x2, f4_derivative_x3, f4_derivative_x4]
}


def coordinate_descent_method(f, eps=10 ** -4, norm=0):
    arguments = f.__code__.co_argcount
    if norm == 0:
        x = initialise_arguments(f)
    else:
        if arguments == 2:
            x = np.full(arguments, norm / 2 ** 0.5)
        elif arguments == 4:
            x = np.full(arguments, norm / 2)
    x_prev = None
    iterations = 0
    while (x_prev is None or not does_converge(x, x_prev, eps)):
        iterations += 1
        alpha = 0.001
        x_prev = x.copy()
        rnd = iterations % arguments
        x[rnd] = x[rnd] - alpha * derivatives[f][rnd](*x_prev)
        print("iteration =", iterations, "\t x =", x)
    return x, iterations


def steepest_descent_method(f, eps=10 ** -4, norm=0):
    arguments = f.__code__.co_argcount
    if norm == 0:
        x = initialise_arguments(f)
    else:
        if arguments == 2:
            x = np.full(arguments, norm / 2 ** 0.5)
        elif arguments == 4:
            x = np.full(arguments, norm / 2)
    x_prev = None
    iterations = 0
    while (x_prev is None or not does_converge(x, x_prev, eps)):
        iterations += 1
        alpha = 0.001
        x_prev = x.copy()
        for i in range(arguments):
            x[i] = x[i] - alpha * derivatives[f][i](*x_prev)
        print("iteration =", iterations, "\t x =", x)
    return x, iterations


def build_graph_from_eps(method, f):
    eps_values = [10 ** i for i in range(-7, 1)]
    iterations_values = []
    for eps in eps_values:
        x, iterations = method(f, eps=eps)
        iterations_values.append(iterations)
    plt.plot(eps_values, iterations_values, 'b')
    plt.xlabel("eps")
    plt.ylabel("iterations")
    plt.xscale('log')
    plt.show()


def build_graph_from_norm(method, f):
    norm_values = [0.25 * i for i in range(13)]
    iterations_values = []
    for norm in norm_values:
        x, iterations = method(f, norm=norm)
        iterations_values.append(iterations)
    plt.plot(norm_values, iterations_values, '#B124E5')
    plt.xlabel("norm")
    plt.ylabel("iterations")
    plt.show()


def brent_method():
    pass


# build_graph_from_eps(coordinate_descent_method, f4)
build_graph_from_norm(coordinate_descent_method, f4)
