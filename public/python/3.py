import numpy as np

EPS = 1e-6

def sample_system(_):
    a = np.array([
        [0, 0, 4],
        [1, 2, 3],
        [0, 1, 2]
    ])
    s = np.array([3, 2, 1])
    b = a @ s
    return a, b, s

def random_system(n):
    a = np.random.uniform(-99, 100, (n, n))
    s = np.random.uniform(-99, 100, n)
    b = a @ s
    return a, b, s

def householder(a_init, b_init=None):
    a = a_init.copy()
    if b_init is not None:
        b = b_init.copy()
    n = len(a)
    q_tilda = np.identity(n)
    u = np.empty(n)
    for r in range(n - 1):
        sigma = sum([a[i][r] ** 2 for i in range(r, n)])
        if sigma <= EPS:
            break
        k = np.sqrt(sigma)
        if a[r][r] > 0:
            k *= -1
        beta = sigma - k * a[r][r]
        u[r] = a[r][r] - k
        for i in range(r + 1, n):
            u[i] = a[i][r]
        for j in range(r + 1, n):
            gamma = sum([u[i] * a[i][j] for i in range(r, n)]) / beta
            for i in range(r, n):
                a[i][j] -= gamma * u[i]
        a[r][r] = k
        for i in range(r + 1, n):
            a[i][r] = 0
        if b_init is not None:
            gamma = sum([u[i] * b[i] for i in range(r, n)]) / beta
            for i in range(r, n):
                b[i] -= gamma * u[i]
        for j in range(n):
            gamma = sum([u[i] * q_tilda[i][j] for i in range(r, n)]) / beta
            for i in range(r, n):
                q_tilda[i][j] -= gamma * u[i]
    q = np.transpose(q_tilda)
    r = a.copy()
    return q, r

def inverse_substitution(a, b):
    n = len(a)
    x = np.empty(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - sum([a[i][j] * x[j] for j in range(i + 1, n)])) / a[i][i]
    return x

def solve_system(q, r, b):
    return inverse_substitution(r, np.transpose(q) @ b)

def system_errors(a, b, x, s):
    norm1 = np.linalg.norm(a @ x - b)
    norm2 = np.linalg.norm(x - s) / np.linalg.norm(s)
    return norm1, norm2

def inverse(q, r):
    n = len(q)
    inv = np.empty((n, n))
    for j in range(n):
        inv[:, j] = inverse_substitution(r, q[j, :])
    return inv

def random_symmetric_matrix(n):
    a = np.empty((n, n))
    for i in range(n):
        for j in range(i, n):
            a[i][j] = a[j][i] = np.random.uniform(-99, 100)
    return a

def limit(a):
    q, r = householder(a)
    while True:
        lim = np.linalg.norm(r @ q - q @ r)
        if lim < EPS:
            break
        q, r = householder(r @ q)
    return lim

def test(n, generate_system):
    a, b, s = generate_system(n)
    print('b =', b)
    print()
    q, r = householder(a, b)
    print('Q =', q)
    print('R =', r)
    print()
    x_hh = solve_system(q, r, b)
    x_qr = solve_system(*np.linalg.qr(a), b)
    print('x_HH =', x_hh)
    print('x_QR =', x_qr)
    print('norm(x_HH - x_QR) == 0:', np.linalg.norm(x_hh - x_qr) < EPS)
    print()
    print('errors(x_HH) == 0:', system_errors(a, b, x_hh, s) < (EPS, EPS))
    print('errors(x_QR) == 0:', system_errors(a, b, x_qr, s) < (EPS, EPS))
    print()
    inv_a_hh = inverse(q, r)
    inv_a_np = np.linalg.inv(a)
    print('inv_A_HH =', inv_a_hh)
    print('inv_A_NP =', inv_a_np)
    print('norm(inv_A_HH - inv_A_NP) == 0:', np.linalg.norm(inv_a_hh - inv_a_np) < EPS)
    print()
    lim = limit(random_symmetric_matrix(n))
    print('lim =', lim)

test(3, sample_system)
# test(5, random_system)
