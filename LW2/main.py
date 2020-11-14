import numpy as np
import random
from matplotlib import pyplot as plt
from matplotlib.collections import LineCollection


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
    return 2 * x1 * (
            x2 ** 6 + x2 ** 4 - 2 * x2 ** 3 - x2 ** 2 - 2 * x2 + 3) + 5.25 * x2 ** 3 + 4.5 * x2 ** 2 + 3 * x2 - 12.75


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


def f5(x):
    return -5 * x ** 5 + 4 * x ** 4 - 12 * x ** 3 + 11 * x ** 2 - 2 * x + 1


def f5_derivative(x):
    return -25 * x ** 4 + 16 * x ** 3 - 36 * x ** 2 + 22 * x - 2


def f6(x):
    return (np.log10(x - 2)) ** 2 + (np.log(10 - x)) ** 2 - x ** 0.2


def f6_derivative(x):
    return 2 / np.log(10) * (np.log10(x - 2) / (x - 2) - np.log10(10 - x) / (10 - x))


def f7(x):
    return -3 * x * np.sin(0.75 * x) + np.exp(-2 * x)


def f7_derivative(x):
    return -2 * np.exp(-2 * x) - 3 * np.sin(0.75 * x) - 2.25 * x * np.cos(0.75 * x)


def f8(x):
    return np.exp(3 * x) + 5 * np.exp(-2 * x)


def f8_derivative(x):
    return np.exp(-2 * x) * (3 * np.exp(5 * x) - 10)


def f9(x):
    return 0.2 * x * np.log10(x) + (x - 2.3) ** 2


def f9_derivative(x):
    return 0.2 * (np.log(x) + 1 / np.log(10)) + 2 * (x - 2.3)


def get_start_and_end(i):
    return {
        1: (-2.0, 2.0),
        2: (-1.0, 1.0),
        3: (-1.0, 3.0)}.get(i)


def get_secant(x1, x2, f1, f2):
    a = (f2 - f1) / (x2 - x1)
    b = f1 - x1 * a
    return - (b / a)


def does_converge(a, b, eps):
    return np.linalg.norm(np.subtract(a, b)) < eps


def initialise_arguments(f):
    if f == f1:
        return np.array([-1.0, -1.0])
    elif f == f2:
        return np.array([-1.0, -1.0])
    elif f == f3:
        return np.array([-2.0, -2.0])
    elif f == f4:
        return np.array([-3.0, -3.0, -3.0, -3.0])


def transform_list(lst):
    new_list = []
    for i in range(len(lst) - 1):
        new_list.append([lst[i], lst[i + 1]])
    return new_list


def draw_plane(f, method):
    delta = 0.025
    bounds = get_start_and_end(1)
    x = np.arange(bounds[0], bounds[1], delta)
    X, Y = np.meshgrid(x, x)
    Z = f(X, Y)
    fig, ax = plt.subplots()
    cs = ax.contour(X, Y, Z)
    ax.clabel(cs)
    x, iterations, history = method(f)
    history = transform_list(history)
    lc = LineCollection(history, linewidths=2, color="blue")
    ax.add_collection(lc)
    ax.margins(0.1)
    plt.show()


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
    history = []
    while (x_prev is None or not does_converge(x, x_prev, eps)):
        iterations += 1
        alpha = 0.001
        x_prev = x.copy()
        history.append(x_prev.copy())
        rnd = iterations % arguments
        x[rnd] = x[rnd] - alpha * derivatives[f][rnd](*x_prev)
        print("iteration =", iterations, "\t x =", x)
    return x, iterations, history


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
    history = []
    while (x_prev is None or not does_converge(x, x_prev, eps)):
        iterations += 1
        alpha = 0.001
        x_prev = x.copy()
        history.append(x_prev.copy())
        for i in range(arguments):
            x[i] = x[i] - alpha * derivatives[f][i](*x_prev)
        print("iteration =", iterations, "\t x =", x)
    return x, iterations, history


def brent_method(f, f_derivative, a, c, eps=10 ** -4):
    x = w = v = (a + c) / 2
    f_x = f_w = f_v = f(x)
    f_x_derivative = f_w_derivative = f_v_derivative = f_derivative(x)
    d = e = c - a
    iterations = 0
    while True:
        iterations += 1
        g, e = e, d
        u = None
        if x != w and f_x_derivative != f_w_derivative:
            u = get_secant(x, w, f_x_derivative, f_w_derivative)
            if a + eps <= u <= c - eps and abs(u - x) < g / 2:
                u = u
            else:
                u = None
        if x != v and f_x_derivative != f_v_derivative:
            u2 = get_secant(x, v, f_x_derivative, f_v_derivative)
            if a + eps <= u2 <= c - eps and abs(u2 - x) < g / 2:
                if u is not None and abs(u2 - x) < abs(u - x):
                    u = u2
        if u is None:
            if f_x_derivative > 0:
                u = (a + x) / 2
            else:
                u = (x + c) / 2
        if abs(u - x) < eps:
            u = x + np.sign(u - x) * eps
        d = abs(x - u)
        f_u = f(u)
        f_u_derivative = f_derivative(u)
        if f_u <= f_x:
            if u >= x:
                a = x
            else:
                c = x
            v, w, x = w, x, u
            f_v, f_w, f_x = f_w, f_x, f_u
            f_v_derivative, f_w_derivative, f_x_derivative = f_w_derivative, f_x_derivative, f_u_derivative
        else:
            if u >= x:
                c = u
            else:
                a = u
            if f_u <= f_w or w == x:
                v, w = w, u
                f_v, f_w = f_w, f_u
                f_v_derivative, f_w_derivative = f_w_derivative, f_u_derivative
            elif f_u <= f_v or v == x or v == w:
                v = u
                f_v = f_u
                f_v_derivative = f_u_derivative
        if iterations != 1:
            if abs(prev_u - u) < eps:
                break
        prev_u = u
        print("iteration: ", iterations, "\t", (c + a) / 2)
    x = (c + a) / 2
    print(x, " ", f(x))
    return x, iterations


def build_graph_for_brent_method(f, f_derivative, a, c):
    eps_values = [10 ** i for i in range(-7, 1)]
    iterations_values = []
    for eps in eps_values:
        x, iterations = brent_method(f, f_derivative, a, c, eps)
        iterations_values.append(iterations)
    plt.plot(eps_values, iterations_values, 'orange')
    plt.xlabel("eps")
    plt.ylabel("iterations")
    plt.xscale('log')
    plt.show()



def build_graph_from_eps(method, f):
    eps_values = [10 ** i for i in range(-7, 1)]
    iterations_values = []
    for eps in eps_values:
        x, iterations, history = method(f, eps=eps)
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
        x, iterations, history = method(f, norm=norm)
        iterations_values.append(iterations)
    plt.plot(norm_values, iterations_values, '#B124E5')
    plt.xlabel("norm")
    plt.ylabel("iterations")
    plt.show()


# build_graph_from_eps(coordinate_descent_method, f4)
# build_graph_from_norm(coordinate_descent_method, f4)
# build_graph_for_brent_method(f9, f9_derivative, 0.5, 2.5)
# for method in [steepest_descent_method, coordinate_descent_method]:
#     for f in [f1, f2, f3]:
#         draw_plane(f, method)
