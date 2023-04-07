import urllib.request
import random
import numpy as np

class SparseMatrix:
    def __init__(self, n):
        self.n = n
        self.matrix = [{} for _ in range(n)]

    def __str__(self):
        return str(self.matrix)

    def add_element(self, i, j, x):
        self.matrix[i][j] = self.matrix[i].setdefault(j, 0) + x

    def dict_to_list(self):
        self.values = []
        self.column = []
        self.start_row = [0]
        for i in range(self.n):
            for j, val in self.matrix[i].items():
                self.values += [val]
                self.column += [j]
            self.start_row += [self.start_row[-1] + len(self.matrix[i])]

    def check_symmetry(self):
        for i in range(self.n):
            for j, val in self.matrix[i].items():
                if self.matrix[j][i] is None or abs(val - self.matrix[j][i]) > 1e-8:
                    return False
        return True

    def generate(self, chance):
        self.matrix = [{} for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                dice = random.randint(0, chance)
                if dice == 0:
                    rand = random.randint(0, 10000)
                    self.matrix[i][j] = self.matrix[j][i] = self.matrix[i].setdefault(j, 0) + rand
        return self.matrix

    def product(self, x):
        p = [0] * self.n
        for i in range(self.n):
            for j, val in self.matrix[i].items():
                p[i] += val * x[j]
        return np.array(p)

    def product2(self, x):
        p = [0] * self.n
        for i in range(self.n):
            for j, col in enumerate(self.column[self.start_row[i]:self.start_row[i + 1]]):
                p[i] += self.values[j + self.start_row[i]] * x[col]
        return np.array(p)

    def power_method(self, prod=1):
        if prod != 1:
            self.dict_to_list()
        x = np.random.uniform(-10, 10, size=(self.n,))
        v = x / np.linalg.norm(x)
        w = self.product(v) if prod == 1 else self.product2(v)
        l = w @ v
        k = 0
        while np.linalg.norm(w - l * v) > self.n * 1e-9 and k <= 1000000:
            v = w / np.linalg.norm(w)
            w = self.product(v) if prod == 1 else self.product2(v)
            l = w @ v
            k += 1
        return l, k

def make_file_url(dim):
    if dim in [512, 1024, 2023]:
        return f'https://profs.info.uaic.ro/~ancai/CN/lab/5/msr/m_rar_sim_2023_{dim}.txt'
    return None

def load_system(dim):
    file = make_file_url(dim)
    content = urllib.request.urlopen(file).read().decode('utf-8').split('\n')
    n = int(content[0])
    matrix = SparseMatrix(n)
    for line in content[1:]:
        val = line.split(',')
        if len(val) != 3: continue
        x = float(val[0].strip())
        i = int(val[1].strip())
        j = int(val[2].strip())
        matrix.add_element(i, j, x)
    return matrix

def svd_decomposition(a):
    p = len(a)
    n = len(a[0])
    u, s, vh = np.linalg.svd(a)

    print('singular values:', s)
    s = np.array([i for i in s if i > 1e-9])
    r = len(s)
    print('rank:', r)
    print('condition number:', max(s) / min(s))

    si = np.pad(np.diag(np.ones((r,)) / s), [(0, n - r), (0, p - n)])
    ai = np.transpose(vh) @ si @ np.transpose(u)
    print('moore-penrose pseudoinverse:', ai)

    b = np.random.rand(p,)
    x = ai @ b
    print('solution:', x)
    print('norm(b - ax):', np.linalg.norm(b - a @ x, ord=2))

    at = np.transpose(a)
    aj = np.linalg.inv(at @ a) @ at
    print('norm(aj - ai):', np.linalg.norm(ai - aj, ord=1))

if __name__ == '__main__':
    for dim in [512, 1024]: # 2023
        a = load_system(dim)
        print(dim, 'symmetric' if a.check_symmetry() else 'asymmetric')
        l, k = a.power_method()
        print(f'lambda: {l} | k: {k}')
        l, k = a.power_method(prod=2)
        print(f'lambda: {l} | k: {k}')
        print()

    n = 800
    b = SparseMatrix(n)
    b.generate(10)
    print(n, 'symmetric' if b.check_symmetry() else 'asymmetric')
    l, k = b.power_method()
    print(f'lambda: {l} | k: {k}')
    l, k = b.power_method(prod=2)
    print(f'lambda: {l} | k: {k}')
    print()

    a = np.random.rand(4, 3)
    svd_decomposition(a)
