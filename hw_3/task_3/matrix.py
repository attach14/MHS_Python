#в качестве хэша матрицы берем её след
#Пример коллизии: единичная матрица и верхнетреугольная матрица с единицами на главной диагонали


class TraceHashMixin:
    def __hash__(self):
        return hash(sum(self.data[i][i] for i in range(min(self.shape))))


class MatrixHash(TraceHashMixin):
    _matmul_cache = {}
    def __init__(self, data):
        if hasattr(data, 'tolist'):
            data = data.tolist()
        if not data or not data[0]:
            raise ValueError("Empty matrix")
        row_len = len(data[0])
        if any(len(row) != row_len for row in data):
            raise ValueError("Rows must have equal length")
        self.data = [list(row) for row in data]
        self.shape = (len(self.data), row_len)

    def __add__(self, other):
        if self.shape != other.shape:
            raise ValueError("Shape mismatch")
        result = [
            [self.data[i][j] + other.data[i][j] for j in range(self.shape[1])]
            for i in range(self.shape[0])
        ]
        return MatrixHash(result)

    def __mul__(self, other):
        if self.shape != other.shape:
            raise ValueError("Shape mismatch")
        result = [
            [self.data[i][j] * other.data[i][j] for j in range(self.shape[1])]
            for i in range(self.shape[0])
        ]
        return MatrixHash(result)

    def __matmul__(self, other):
        if self.shape[1] != other.shape[0]:
            raise ValueError("Shape mismatch")
        
        key = (hash(self), hash(other))
        if key in MatrixHash._matmul_cache:
            return MatrixHash._matmul_cache[key]

        rows, mid, cols = self.shape[0], self.shape[1], other.shape[1]
        result = []
        for i in range(rows):
            row = []
            for j in range(cols):
                s = 0
                for k in range(mid):
                    s += self.data[i][k] * other.data[k][j]
                row.append(s)
            result.append(row)
        
        MatrixHash._matmul_cache[key] = MatrixHash(result)
        return MatrixHash(result)
    
    def __eq__(self, other):
        return isinstance(other, MatrixHash) and self.data == other.data
    __hash__ = TraceHashMixin.__hash__

    @staticmethod
    def clear_cache():
        MatrixHash._matmul_cache.clear()