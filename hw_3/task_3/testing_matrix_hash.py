from matrix import MatrixHash
from os.path import dirname, abspath, join

def mat_to_file(matrix, filename):
    with open(filename, 'w') as f:
        for row in matrix.data:
            f.write('\t'.join(str(x) for x in row) + '\n')

A = MatrixHash([[1, 2], [3, 4]])
C = MatrixHash([[2, 2], [3, 3]])
assert hash(A) == hash(C)
assert A != C
B = MatrixHash([[1, 0], [0, 1]])
D = MatrixHash([[1, 0], [0, 1]])
assert B == D
AB = A @ B
CD_cached = C @ D
assert AB == CD_cached
A.clear_cache()
CD_true = C @ D

mat_to_file(A, abspath(join(dirname(__file__), '../artifacts/A.txt')))
mat_to_file(B, abspath(join(dirname(__file__), '../artifacts/B.txt')))
mat_to_file(C, abspath(join(dirname(__file__), '../artifacts/C.txt')))
mat_to_file(D, abspath(join(dirname(__file__), '../artifacts/D.txt')))
mat_to_file(AB, abspath(join(dirname(__file__), '../artifacts/AB.txt')))
mat_to_file(CD_true, abspath(join(dirname(__file__), '../artifacts/CD_true.txt')))
with open(abspath(join(dirname(__file__), '../artifacts/hash.txt')), 'w') as f:
    f.write(f"hash(AB) = {hash(AB)}\n")
    f.write(f"hash(CD_true) = {hash(CD_true)}\n")
    f.write(f"hash(CD_cached) = {hash(CD_cached)}\n")