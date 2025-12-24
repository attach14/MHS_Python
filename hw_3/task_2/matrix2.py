import numpy as np
from numpy.lib.mixins import NDArrayOperatorsMixin

class StrMixin:
    def __str__(self):
        return '\n'.join('\t'.join(str(v) for v in row) for row in self.data)

class FileMixin:
    def to_file(self, filename):
        with open(filename, "w") as f:
            f.write(str(self) + '\n')

class PropertyMixin:
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, val):
        self._data = np.asarray(val)

    @property
    def shape(self):
        return self._data.shape

class Matrix(NDArrayOperatorsMixin, StrMixin, FileMixin, PropertyMixin):
    def __init__(self, data):
        self.data = np.asarray(data)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        arrays = []
        for x in inputs:
            if isinstance(x, Matrix):
                arrays.append(x.data)
            else:
                arrays.append(x)
        result = getattr(ufunc, method)(*arrays, **kwargs)
        if isinstance(result, tuple):
            return tuple(Matrix(x) if isinstance(x, np.ndarray) else x for x in result)
        elif isinstance(result, np.ndarray):
            return Matrix(result)
        else:
            return result

    def __array__(self, dtype=None):
        return np.asarray(self.data, dtype=dtype)