import math
import random

def sign(x):
    return 1 if x >= 0 else -1

def horner(p, x0):
    y0 = 0
    for ai in p[::-1]:
        y0 = ai + y0 * x0
    return y0

def derivative(p):
    pp = []
    for ai, i in enumerate(p[1:], 1):
        pp += [ai * i]
    return pp

p = random.sample(range(-100, 100), 10)
n = len(p) - 1
pp = derivative(p)
ppp = derivative(pp)

x = []
k = 0
k_max = 1000
while True:
    r = (abs(p[0]) + max(p[1:])) / abs(p[0])
    xk = random.uniform(-r, r)
    delta_xk = -1
    while True:
        h_xk = (n - 1) ** 2 * horner(pp, xk) ** 2 - n * (n - 1) * horner(p, xk) * horner(ppp, xk)
        if h_xk < 0: break
        num = horner(pp, xk) + sign(horner(pp, xk)) * math.sqrt(h_xk)
        if abs(num) < 1e-3: break
        delta_xk = n * horner(p, xk) / num
        xk -= delta_xk
        if abs(delta_xk) < 1e-3 or k > k_max or abs(delta_xk) > 1e8: break
        k += 1
    if abs(delta_xk) < 1e-3:
        new = True
        for xi in x:
            if abs(xi - xk) < 1e-3:
                new = False
                break
        if new:
            print(xk, horner(p, xk))
            x += [xk]
