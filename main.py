import numpy as np

def generate(n):
    a = np.zeros((n, n))
    for i in range(n):
        a[i][i] = np.random.uniform(0, 100)
        for j in range(i):
            a[i][j] = a[j][i] = np.random.uniform(-100, 100)
    for i in range(n):
        a[i][i] += sum([abs(x) for x in a[i]]) - abs(a[i][i])
    b = np.random.rand(n)
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
        x[i] = b[i] - sum([a[i][j] * x[j] for j in range(i + 1, n)])
    return x

eps = 1e-6
a_init = np.array([
    [1.0, 2.5, 3.0],
    [2.5, 8.25, 15.5],
    [3.0, 15.5, 43.0]
])
b = np.array([12, 38, 68])

# a, b = generate(3)

a, d = decompose(a_init)
print(d)
det = np.prod(d)

z = direct_substitution(a, b)
y = z / d
x = inverse_substitution(a, y)
print(x)
