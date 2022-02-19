from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        for i in range(len(matrix) - 1):
            if len(matrix[i]) != len(matrix[i + 1]):
                raise ValueError('fail initialization matrix')

    def __str__(self):
        matrix_str = ''
        for some_el in self.matrix:
            el_str = ' '.join(map(str, some_el))
            el_str = f'| {el_str} |\n'
            matrix_str += el_str
        return matrix_str

    def __add__(self, other):
        matrix_list = []
        for i in range(len(self.matrix)):
            matrix_el = []
            for k in range(len(self.matrix[i])):
                new_el = self.matrix[i][k] + other.matrix[i][k]
                matrix_el.append(new_el)
            matrix_list.append(matrix_el)
        matrix_list = Matrix(matrix_list)
        return matrix_list


if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(first_matrix)
    """
    | 1 2 |
    | 3 4 |
    | 5 6 |
    """
    print(first_matrix + second_matrix)
    """
    | 7 7 |
    | 7 7 |
    | 7 7 |
    """
    fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
    """
    Traceback (most recent call last):
      ...
    ValueError: fail initialization matrix
    """
