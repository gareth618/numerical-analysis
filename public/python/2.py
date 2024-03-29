import numpy as np
import scipy.linalg as la

def is_diagonal_dominant(a):
    for i in range(len(a)):
        if a[i][i] <= sum([abs(x) for x in a[i]]) - abs(a[i][i]):
            return False
    return True

def generate(n):
    a = np.zeros((n, n))
    for i in range(n):
        a[i][i] = np.random.uniform(0, 100)
        for j in range(i):
            a[i][j] = a[j][i] = np.random.uniform(-99, 100)
    for i in range(n):
        a[i][i] += sum([abs(x) for x in a[i]]) - abs(a[i][i])
    b = np.random.uniform(-99, 100, n)
    return a, b

def decompose(a_init):
    n = len(a_init)
    a = np.copy(a_init)
    d = np.zeros(n)
    for p in range(n):
        d[p] = a[p][p]
        for k in range(p):
            d[p] -= d[k] * a[p][k] ** 2
        for i in range(p + 1, n):
            a[i][p] = (a[i][p] - sum([d[k] * a[i][k] * a[p][k] for k in range(p)])) / d[p]
    return a, d

def direct_substitution(a, b):
    n = len(a)
    x = np.zeros(n)
    for i in range(n):
        x[i] = b[i] - sum([a[i][j] * x[j] for j in range(i)])
    return x

def inverse_substitution(a, b):
    n = len(a)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = b[i] - sum([a[j][i] * x[j] for j in range(i + 1, n)])
    return x

def check_decomposition(a, d):
    def get_ld(i, j):
        if j < i: return d[j] * a[i][j]
        if j == i: return d[j]
        return 0

    def get_lt(i, j):
        if j < i: return 0
        if j == i: return 1
        return a[j][i]

    n = len(a)
    for i in range(n):
        for j in range(i, n):
            a_ij = sum([get_ld(i, k) * get_lt(k, j) for k in range(n)])
            if abs(a_ij - a[i][j]) > 1e-5:
                return False
    return True

def cholesky(a_init, b):
    a, d = decompose(a_init)
    print('valid decomposition?', check_decomposition(a, d))
    print('det(A) =', np.prod(d))
    z = direct_substitution(a, b)
    y = z / d
    x = inverse_substitution(a, y)
    return x

def plu(a_init, b):
    p, l, u = la.lu(a_init)
    y = la.solve(l, p @ b)
    x = la.solve(u, y)
    return x

a_init = np.array([
    [1.0, 2.5, 3.0],
    [2.5, 8.25, 15.5],
    [3.0, 15.5, 43.0]
])
b = np.array([12, 38, 68])

a_init, b = generate(5)
x = cholesky(a_init, b)
norm = np.sqrt(sum([i * i for i in a_init @ x - b]))
print('norm(a_init @ x_chol - b) == 0?', norm < 1e-8)
