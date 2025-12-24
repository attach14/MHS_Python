import numpy as np
from matrix import Matrix
from os.path import dirname, abspath, join

def mat_to_file(matrix, filename):
    with open(filename, 'w') as f:
        for row in matrix.data:
            f.write('\t'.join(str(x) for x in row) + '\n')

np.random.seed(0)

a = Matrix(np.random.randint(0, 10, (10, 10)))
b = Matrix(np.random.randint(0, 10, (10, 10)))

mat_to_file(a + b, abspath(join(dirname(__file__), '../artifacts/3_1_matrix+.txt')))
mat_to_file(a * b, abspath(join(dirname(__file__), '../artifacts/3_1_matrix*.txt')))
mat_to_file(a @ b, abspath(join(dirname(__file__), '../artifacts/3_1_matrix@.txt')))
