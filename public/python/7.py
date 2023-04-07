import math
import cmath
import random

def sign(z):
    return z / abs(z)

def horner(P, z):
    c, d = z.real, z.imag
    p, q = -2 * c, c ** 2 + d ** 2
    a = P[::-1]
    b = []
    b += [a[0]]
    b += [a[1] - p * b[0]]
    for i in range(2, len(a)):
        b += [a[i] - p * b[i - 1] - q * b[i - 2]]
    r0 = b[-2]
    r1 = b[-1] + p * b[-2]
    C = r0 * c + r1
    D = r0 * d
    return complex(C, D)

def derivative(P):
    P1 = []
    for ai, i in enumerate(P[1:], 1):
        P1 += [ai * i]
    return P1

def random_polynomial(n, value):
    return [random.uniform(1, value) * (-1 if random.random() < .5 else +1) for _ in range(n + 1)]

EPS = 1e-3
K_MAX = 100

n = 5
P = random_polynomial(n, 10)
P1 = derivative(P)
P2 = derivative(P1)
print(P)

B = max(abs(ai) for ai in P[:-1])
C = max(abs(ai) for ai in P[1:])
r = 1 / (1 + C / abs(P[0]))
R = 1 + B / abs(P[-1])
A = 2 / (R ** 2 - r ** 2)

z = []
k = 0
while True:
    theta = random.uniform(0, 2 * math.pi)
    radius = math.sqrt(2 * random.random() / A + r ** 2)
    zk = complex(radius * math.cos(theta), radius * math.sin(theta))

    delta_zk = -1
    while True:
        h_zk = (n - 1) ** 2 * horner(P1, zk) ** 2 - n * (n - 1) * horner(P, zk) * horner(P2, zk)
        denominator = horner(P1, zk) + sign(horner(P1, zk)) * cmath.sqrt(h_zk)
        if abs(denominator) < EPS: break
        delta_zk = n * horner(P, zk) / denominator
        zk -= delta_zk
        if abs(delta_zk) < EPS or k > K_MAX or abs(delta_zk) > 1e8: break
        k += 1

    if abs(delta_zk) < EPS:
        new = True
        for zi in z:
            if abs(zi - zk) < EPS:
                new = False
                break
        if new:
            print(zk, abs(horner(P, zk)))
            z += [zk]
