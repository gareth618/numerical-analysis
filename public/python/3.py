import numpy as np

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
    """generăm random matricea A și vectorul s, reprezentând o soluție a sistemului pe care dorim să-l creăm
    apoi, cunoscând A, s și că s este o soluție a sistemului Ax = b, determinăm b-ul drept As
    astfel, ne asigurăm că sistemul pe care-l generăm admite din start o soluție, și anume pe s"""
    a = ...
    s = ...
    b = a @ s
    return a, b, s

def householder(a):
    """descompunem QR matricea A"""
    q = ...
    r = ...
    return q, r

def solve_system(a, b, decompose):
    """decompose este o funcție de callback ce descompune QR matricea A
    descompunerea poate fi cea implementată de noi (householder) sau cea din bibliotecă"""
    q, r = decompose(a)
    x = ...
    return x

def system_errors(a, b, x, s):
    norm1 = ... # folosește A, b, x
    norm2 = ... # folosește x, s
    return norm1, norm2

def inverse(a):
    q, r = householder(a)
    inv = ...
    return inv

def random_symmetric_matrix(n):
    a = ...
    return a

def limit(a):
    """folosim householder la fiecare pas"""
    lim = ...
    return lim

def test(n, generate_system):
    a, b, s = generate_system(n)
    print('b =', b)
    q, r = householder(a)
    print('Q =', q)
    print('R =', r)
    x_hh = solve_system(a, b, householder)
    x_qr = solve_system(a, b, ...)
    print('x_HH =', x_hh)
    print('x_QR =', x_qr)
    print('norm(x_HH - x_QR) =', ...)
    print('errors(x_HH) =', system_errors(a, b, x_hh, s))
    print('errors(x_QR) =', system_errors(a, b, x_qr, s))
    inv_a_hh = inverse(a)
    inv_a_np = ...
    print('norm(inv_A_HH, inv_A_NP) =', ...)
    lim = limit(random_symmetric_matrix(n))
    print('lim =', lim)

test(3, sample_system)
test(5, random_system)
