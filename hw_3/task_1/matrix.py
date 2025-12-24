class Matrix:
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
        return Matrix(result)

    def __mul__(self, other):
        if self.shape != other.shape:
            raise ValueError("Shape mismatch")
        result = [
            [self.data[i][j] * other.data[i][j] for j in range(self.shape[1])]
            for i in range(self.shape[0])
        ]
        return Matrix(result)

    def __matmul__(self, other):
        if self.shape[1] != other.shape[0]:
            raise ValueError("Shape mismatch")
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
        return Matrix(result)