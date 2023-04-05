import random

def f(x):
    res = 0
    for i, c in enumerate(coef[::-1]):
        res += (x ** i) * c
    return res

def g1(x):
    return (3 * f(x) - 4 * f(x - h) + f(x - 2 * h)) / (2 * h)

def g2(x):
    return (-f(x + 2 * h) + 8 * f(x + h) - 8 * f(x - h) + f(x - 2 * h)) / (12 * h)

def f2(x):
    return (-f(x + 2 * h) + 16 * f(x + h) - 30 * f(x) + 16 * f(x - h) - f(x - 2 * h)) / (12 * h * h)

def secant_method(g):
    x0 = random.uniform(-100, 100)
    x1 = random.uniform(-100, 100)
    while x1 == x0:
        x1 = random.uniform(-100, 100)

    k = 0
    eps = 1e-5
    delta_x = 1
    while eps <= abs(delta_x) <= 1e8 and k <= 1000:
        gx1 = g(x1)
        denominator = gx1 - g(x0)
        if eps >= abs(denominator):
            if abs(gx1) <= eps / 100:
                delta_x = 0
            else:
                delta_x = 1e-5
        else:
            delta_x = (x1 - x0) * gx1 / denominator
        x0 = x1
        x1 -= delta_x
        k += 1

    if abs(delta_x) < eps:
        return x1, k
    else:
        return 'divergence', k

if __name__ == '__main__':
    h = 1e-5
    coef = [1 / 3, -2, 2, 3]
    sol1, k1 = secant_method(g1)
    sol2, k2 = secant_method(g2)
    print(k1, sol1, 'minim' if f2(sol1) > 0 else 'maxim')
    print(k2, sol2, 'minim' if f2(sol2) > 0 else 'maxim')
