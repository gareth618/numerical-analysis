import math
import random
import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

examples = [
    [1, 5, lambda x: x ** 2 - 12 * x + 30, 2],
    [0, 1.5, lambda x: math.sin(x) - math.cos(x), 2],
    [0, 2, lambda x: 2 * x ** 3 - 3 * x + 15, 3]
]

def read_n_i():
    try:
        n = int(input('enter n: '))
        i = int(input('enter i: '))
        if n < 1: raise Exception()
        if i not in range(len(examples)): raise Exception()
        return n, i
    except:
        print('[ERROR] bad input')
        exit(1)

def sample_nodes(x0, xn, n, f):
    interpolator = interp1d([0, n], [x0, xn])
    x_int = [0, *sorted(random.sample(range(1, n), n - 1)), n]
    x_float = [interpolator(x).tolist() for x in x_int]
    return x_float, [f(x) for x in x_float]

def lagrange(x, y, x_test):
    aitken = []
    for i in range(n + 1):
        aitken += [[0] * i + [y[i]] + [0] * (n - i)]
    for l in range(2, n + 2):
        for i, j in zip(range(n - l + 2), range(l - 1, n + 1)):
            aitken[i][j] = (aitken[i + 1][j] - aitken[i][j - 1]) / (x[j] - x[i])
    y_test = 0
    product = 1
    for i in range(len(x)):
        y_test += aitken[0][i] * product
        product *= x_test - x[i]
    return y_test

def lagrange_optimized(x, y, x_test):
    # aitken[i][j] -> aitken[j - i + 1][i]
    aitken = [[0] * (n + 1), [*y]]
    index = 1
    y_test = aitken[index][0]
    product = 1
    for l in range(2, n + 2):
        index = 1 - index
        for i in range(n - l + 2):
            aitken[index][i] = (aitken[1 - index][i + 1] - aitken[1 - index][i]) / (x[i + l - 1] - x[i])
        product *= x_test - x[l - 2]
        y_test += aitken[index][0] * product
    return y_test

def least_squares(x, y, m):
    b = np.empty((m + 1, m + 1))
    for i in range(m + 1):
        for j in range(m + 1):
            b[i][j] = sum([xk ** (i + j) for xk in x])
    f = np.empty(m + 1)
    for i in range(m + 1):
        f[i] = sum([yk * xk ** i for xk, yk in zip(x, y)])
    return la.solve(b, f)

def horner(a, x_test):
    y_test = 0
    for ai in a[::-1]:
        y_test = ai + y_test * x_test
    return y_test

n, i = read_n_i()
x0, xn, f, m = examples[i]
x, y = sample_nodes(x0, xn, n, f)
x_test = random.uniform(x0, xn)

print('x:', x)
print('y:', y)
y_test_lagrange = lagrange_optimized(x, y, x_test)
print(x_test, y_test_lagrange, abs(y_test_lagrange - f(x_test)))
a_least_squares = least_squares(x, y, m)
print(x_test, abs(horner(a_least_squares, x_test) - f(x_test)), sum([abs(horner(a_least_squares, xi) - f(xi)) for xi in x]))

x0 = 0
xn = 10

lx, ly = [], []
xi = x0
while xi <= xn:
    lx += [xi]
    ly += [lagrange_optimized(x, y, xi)]
    xi += .01
plt.plot(lx, ly)

px, py = [], []
xi = x0
while xi <= xn:
    px += [xi]
    py += [horner(a_least_squares, xi)]
    xi += .01
plt.plot(px, py)
plt.show()
