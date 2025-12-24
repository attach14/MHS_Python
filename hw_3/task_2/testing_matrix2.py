import numpy as np
from matrix2 import Matrix
from os.path import dirname, abspath, join

np.random.seed(0)

a = Matrix(np.random.randint(0, 10, (10, 10)))
b = Matrix(np.random.randint(0, 10, (10, 10)))

(a + b).to_file(abspath(join(dirname(__file__), '../artifacts/3_2_matrix+.txt')))
(a * b).to_file(abspath(join(dirname(__file__), '../artifacts/3_2_matrix*.txt')))
(a @ b).to_file(abspath(join(dirname(__file__), '../artifacts/3_2_matrix@.txt')))
