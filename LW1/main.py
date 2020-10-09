from math import log10, log2, sin, e
from matplotlib import pyplot as plt
import csv


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
    plt.grid()
    plt.show()


def build_function(function, X, y_name='y', color='r'):
    Y = []
    for x in X:
        Y.append(function(x))
    draw_function(X, Y, 'x', y_name, color)


def build_functions():
    build_function(f1, [0.01 * x for x in range(-50, 50)], 'y', 'b')
    build_function(f2, [0.01 * x for x in range(600, 990)], 'y', 'g')
    build_function(f3, [0.01 * x for x in range(0, 628)], 'y', 'r')
    build_function(f4, [0.01 * x for x in range(0, 100)], 'y', 'c')
    build_function(f5, [0.01 * x for x in range(50, 250)], 'y', 'm')


def dichotomy_method(f, a, b, eps, filename='file.csv'):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['i', 'a', 'b', 'b - a', 'k', 'x1', 'x2', 'y1', 'y2'])
        delta = 0.49 * eps
        previous_length = 0
        i = 0
        c = 4
        while b - a > eps:
            i += 1
            x1 = (a + b) / 2 - delta
            x2 = (a + b) / 2 + delta
            writer.writerow([i, round(a, c), round(b, c), round(b - a, c), round(previous_length / (b - a), c),
                             round(x1, c), round(x2, c), round(f(x1), c), round(f(x2), c)])
            previous_length = b - a
            if f(x1) < f(x2):
                b = x2
            else:
                a = x1
    return (a + b) / 2, f((a + b) / 2), i


def golden_ratio_method(f, a, b, eps, filename='file.csv'):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['i', 'a', 'b', 'b - a', 'k', 'x1', 'x2', 'y1', 'y2'])
        golden_ratio = 0.5 * (3 - 5 ** 0.5)
        previous_length = 0
        i = 0
        c = 4
        x1 = a + golden_ratio * (b - a)
        x2 = b - golden_ratio * (b - a)
        y1 = f(x1)
        y2 = f(x2)
        while b - a > eps:
            i += 1
            writer.writerow([i, round(a, c), round(b, c), round(b - a, c), round(previous_length / (b - a), c),
                             round(x1, c), round(x2, c), round(y1, c), round(y2, c)])
            previous_length = b - a
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
        return (a + b) / 2, f((a + b) / 2), i


def parabolic_minimum(x1, x2, x3, y1, y2, y3):
    return x2 - 0.5 * ((x2 - x1) ** 2 * (y2 - y3) - (x2 - x3) ** 2 * (y2 - y1)) / (
            (x2 - x1) * (y2 - y3) - (x2 - x3) * (y2 - y1))


def parabolic_interpolation_method(f, a, b, eps, filename='file.csv'):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['i', 'x1', 'x2', 'x3', 'x3 - x1', 'k', 'y1', 'y2', 'y3'])
        previous_length = 0
        i = 0
        c = 4
        x1, x2, x3 = a, (a + b) / 2, b
        y1, y2, y3 = f(x1), f(x2), f(x3)
        while x3 - x1 >= eps:
            i += 1
            writer.writerow(
                [i, round(x1, c), round(x2, c), round(x3, c), round(x3 - x1, c), round(previous_length / (x3 - x1), c),
                 round(y1, c), round(y2, c), round(y3, c)])
            previous_length = x3 - x1
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
        return (x1 + x3) / 2, f((x1 + x3) / 2), i


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


def fibonachi(n):
    if n in (1, 2):
        return 1
    return fibonachi(n - 1) + fibonachi(n - 2)


def fibonachi_method(f, a, b, eps, filename='file.csv', n=20):
    def dot(a, b, n, k, is_first):
        if is_first:
            return a + (fibonachi(n - k - 1) * (b - a)) / fibonachi(n - k + 1)
        else:
            return a + (fibonachi(n - k) * (b - a)) / fibonachi(n - k + 1)

    l = dot(a, b, n, 1, True)
    r = dot(a, b, n, 1, False)
    i = 0
    for k in range(2, n + 1):
        i += 1
        prev = (l, r)
        if f(l) > f(r):
            a = l
            l = r
            r = dot(a, b, n, k, False)
        else:
            b = r
            r = l
            l = dot(a, b, n, k, True)
        if k == n - 2:
            break
    return (l + r) / 2, f((l + r) / 2), i


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
        [f1, -0.5, 0.5, 0.05],
        [f2, 6, 9.9, 1],
        [f3, 0, 6.28, 0.314],
        [f4, 0, 1, 0.05],
        [f5, 0.5, 2.5, 0.1]
    ]
    methods = [fibonachi_method]
    for row in functions:
        print("Function: " + str(row[0].__name__))
        for method in methods:
            x, y, i = method(row[0], row[1], row[2], row[3], str(method.__name__) + "_" + str(row[0].__name__) + ".csv")
            print(method.__name__ + ": x =", x, "\ty =", y, "\ti =", i)
        real_result = get_min(row[0], row[1], row[2], row[3])
        print("real result =", real_result)
        print("=======================================")


number_to_color = {
    1: 'b',
    2: 'g',
    3: 'r',
    4: 'c',
    5: 'm'
}


def build_graph_i_of_log2_eps(function_number, method):
    functions = [
        [f1, -0.5, 0.5],
        [f2, 6, 9.9],
        [f3, 0, 6.28],
        [f4, 0, 1],
        [f5, 0.5, 2.5]
    ]
    f = function_number - 1
    eps_list = [0.00001 * 2 ** j for j in range(16)]
    log2_eps_list = [log2(eps) for eps in eps_list]
    i_list = []
    for eps in eps_list:
        x, y, i = method(functions[f][0], functions[f][1], functions[f][2], eps)
        if str(method.__name__) == 'dichotomy_method':
            i *= 2
        elif str(method.__name__) == 'golden_ratio_method':
            if i != 0:
                i += 2
        elif str(method.__name__) == 'parabolic_interpolation_method':
            if i != 0:
                i += 3
        elif str(method.__name__) == 'brent_method':
            i += 1
        i_list.append(i)
    draw_function(log2_eps_list, i_list, 'log2(eps)', 'i', number_to_color[function_number])


# find_all_min()
for i in [1, 2, 3, 4, 5]:
    for method in [golden_ratio_method]:
        build_graph_i_of_log2_eps(i, method)
