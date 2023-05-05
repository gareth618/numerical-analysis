import numpy as np
# import urllib.request
from copy import deepcopy

class SparseMatrix:
    def __init__(self, n):
        self.n = n
        self.matrix = [{} for _ in range(n)]

    def __str__(self):
        return str(self.matrix)

    def __add__(self, other):
        s = SparseMatrix(self.n)
        s.matrix = deepcopy(self.matrix)
        for i in range(self.n):
            for j, val in other.matrix[i].items():
                s.add_element(i, j, val)
        return s

    def __eq__(self, other):
        for i in range(self.n):
            for j, val in self.matrix[i].items():
                if j not in other.matrix[i] and val != 0:
                    return False
                if j in other.matrix[i] and abs(val - other.matrix[i][j]) > 1e-8:
                    return False
            for j in other.matrix[i]:
                if j not in self.matrix[i]:
                    return False
        return True

    def add_element(self, i, j, x):
        self.matrix[i][j] = self.matrix[i].setdefault(j, 0) + x

    def check_diagonal(self):
        for i, row in enumerate(self.matrix):
            if i not in row:
                return False
        return True

    def compress(matrix):
        n = len(matrix)
        a = SparseMatrix(n)
        for i in range(n):
            for j in range(n):
                if matrix[i][j] != 0:
                    a.add_element(i, j, matrix[i][j])
        return a

    def solve_system(self, b, x=None):
        if x is None:
            x = [0] * self.n
        k = 0
        kmax = 10000
        delta_x = 10
        while k < kmax and 1e-6 <= delta_x <= 1e8:
            xp = x.copy()
            for i in range(self.n):
                sum1 = sum([self.matrix[i][j] * x[j] for j in self.matrix[i] if j < i])
                sum2 = sum([self.matrix[i][j] * xp[j] for j in self.matrix[i] if i < j < self.n])
                x[i] = (b[i] - sum1 - sum2) / self.matrix[i][i]
            delta_x = np.linalg.norm(np.array(x) - np.array(xp))
            k += 1
        if delta_x < 1e-6:
            product = [0] * self.n
            for i in range(self.n):
                for j, val in self.matrix[i].items():
                    product[i] += val * x[j]
            norm = np.linalg.norm(np.array(product) - np.array(b), ord=np.inf)
            print('norm(A @ xGS - b) = 0:', norm < 1e-6)
            return x
        else:
            return 'divergence'

def make_file_urls(index):
    file_a = f'https://profs.info.uaic.ro/~ancai/CN/lab/4/sislinrar/a_{index + 1}.txt'
    file_b = f'https://profs.info.uaic.ro/~ancai/CN/lab/4/sislinrar/b_{index + 1}.txt'
    return file_a, file_b

# def load_sparse_matrix(file):
#     content_a = urllib.request.urlopen(file).read().decode('utf-8').split('\n')
#     n = int(content_a[0])
#     a = SparseMatrix(n)
#     for line in content_a[1:]:
#         val = line.split(',')
#         if len(val) != 3: continue
#         x = float(val[0].strip())
#         i = int(val[1].strip())
#         j = int(val[2].strip())
#         a.add_element(i, j, x)
#     return a

# def load_system(file_index):
#     file_a, file_b = make_file_urls(file_index)
#     a = load_sparse_matrix(file_a)
#     content_b = urllib.request.urlopen(file_b).read().decode('utf-8').split('\n')
#     b = [float(val) for val in content_b[1:] if len(val.strip()) > 0]
#     return a, b

# def test_addition():
#     file_a = f'https://profs.info.uaic.ro/~ancai/CN/lab/4/sislinrar/a.txt'
#     file_b = f'https://profs.info.uaic.ro/~ancai/CN/lab/4/sislinrar/b.txt'
#     file_s = f'https://profs.info.uaic.ro/~ancai/CN/lab/4/sislinrar/aplusb.txt'
#     a = load_sparse_matrix(file_a)
#     b = load_sparse_matrix(file_b)
#     s = load_sparse_matrix(file_s)
#     print('a + b = s:', a + b == s)

if __name__ == '__main__':
    file_count = 5

    make_solution = [
        lambda n: [1] * n,
        lambda n: [4 / 3] * n,
        lambda n: [2 * i / 5 for i in range(n)],
        lambda n: [i / 7 for i in range(n)],
        lambda n: [2] * n
    ]

    # a = SparseMatrix.compress([
    #     [102.5, 0, 2.5, 0, 0],
    #     [3.5, 104.88, 1.05, 0, 0.33],
    #     [0, 0, 100, 0, 0],
    #     [0, 1.3, 0, 101.3, 0],
    #     [0.73, 0, 0, 1.5, 102.23]
    # ])

    # x = [1, 2, 3, 4, 5]
    # b = [6, 7, 8, 9, 1]

    # print(a.solve_system(b, x))
    # for i in range(file_count):
    #     a, b = load_system(i)
    #     if a.check_diagonal():
    #         x = a.solve_system(b)
    #         if x != 'divergence':
    #             norm = np.linalg.norm(np.array(x) - np.array(make_solution[i](a.n)))
    #             print(f'[{i + 1}]', 'norm = 0:', norm < 1e-6)
    #         else:
    #             print(f'[{i + 1}]', x)

    # test_addition()

def random_system(n):
    a = np.random.uniform(-99, 100, (n, n))
    s = np.random.uniform(-99, 100, n)
    b = a @ s
    return a, b

def solve_system(a, b):
    sol = SparseMatrix.compress(a).solve_system(b)
    return np.array([] if sol == 'divergence' else sol)
