import numpy as np

def fun1(u):
    print(1 + u == 1)

def fun2(u):
    x = 10.0
    y = u
    z = u
    print((x + y) + z == x + (y + z))
    print((x * y) * z == x * (y * z))

def strassen(a, b, nmin):
    n = len(a)
    if n == nmin:
        return a @ b
    m = n // 2

    def divide(matrix):
        matrix11 = matrix[0:m, 0:m]
        matrix12 = matrix[0:m, m:n]
        matrix21 = matrix[m:n, 0:m]
        matrix22 = matrix[m:n, m:n]
        return matrix11, matrix12, matrix21, matrix22

    a11, a12, a21, a22 = divide(a)
    b11, b12, b21, b22 = divide(b)

    p1 = strassen(a11 + a22, b11 + b22, nmin)
    p2 = strassen(a21 + a22, b11, nmin)
    p3 = strassen(a11, b12 - b22, nmin)
    p4 = strassen(a22, b21 - b11, nmin)
    p5 = strassen(a11 + a12, b22, nmin)
    p6 = strassen(a21 - a11, b11 + b12, nmin)
    p7 = strassen(a12 - a22, b21 + b22, nmin)

    c = np.zeros((n, n))
    c[0:m, 0:m] = p1 + p4 - p5 + p7
    c[0:m, m:n] = p3 + p5
    c[m:n, 0:m] = p2 + p4
    c[m:n, m:n] = p1 + p3 - p2 + p6
    return c

a = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

b = np.array([
    [1, 3, 5, 7],
    [2, 4, 6, 8],
    [9, 11, 13, 15],
    [10, 12, 14, 16]
])

u = 1e-15
fun1(u)
fun2(u)
print(strassen(a, b, 2))
print(a @ b)
