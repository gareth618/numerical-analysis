file_count = 5

def make_file_url(index):
    file_a = f'https://profs.info.uaic.ro/~ancai/CN/lab/4/sislinrar/a_{index + 1}.txt'
    file_b = f'https://profs.info.uaic.ro/~ancai/CN/lab/4/sislinrar/b_{index + 1}.txt'
    return file_a, file_b

make_solution = [
    lambda n: [1] * n,
    lambda n: [4 / 3] * n,
    lambda n: [2 * i / 5 for i in range(n)],
    lambda n: [i / 7 for i in range(n)],
    lambda n: [2] * n
]

class SparseMatrix:
    def __init__(self, n):
        self.n = n
        self.matrix = [{ } for _ in range(n)]

    def add_element(self, i, j, x):
        self.matrix[i][j] = x

    def compress(matrix):
        n = len(matrix)
        a = SparseMatrix(n)
        for i in range(n):
            for j in range(n):
                a.add_element(i, j, matrix[i][j])
        return a

    def solve_system(self, b, x = None):
        if x is None:
            x = [0] * self.n
        x = [...]
        return x

def load_system(file_index):
    file_a, file_b = make_file_url(file_index)
    a = SparseMatrix(...)
    b = [...]
    return a, b

a = SparseMatrix.compress([
    [102.5, 0, 2.5, 0, 0],
    [3.5, 104.88, 1.05, 0, .33],
    [0, 0, 100, 0, 0],
    [0, 1.3, 0, 101.3, 0],
    [.73, 0, 0, 1.5, 102.23]
])

x = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 1]

print(a.solve_system(b, x))
for i in range(file_count):
    a, b = load_system(i)
    x = a.solve_system(b)
    print(x, make_solution[i](a.n))
