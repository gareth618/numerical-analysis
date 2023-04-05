import random

def generate_symmetric_sparse_matrix(n):
    matrix = [{} for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dice = random.randint(0, 99)
            if dice == 0:
                rand = random.randint(0, 10000)
                matrix[i][j] = matrix[j][i] = matrix[i].setdefault(j, 0) + rand
    return matrix

a = generate_symmetric_sparse_matrix(1000)
