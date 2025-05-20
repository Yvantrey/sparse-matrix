from sparse_matrix import SparseMatrix

def transpose_matrix(matrix):
    result = SparseMatrix(rows=matrix.cols, cols=matrix.rows)

    for row in matrix.data:
        for col, value in matrix.data[row].items():
            result.set_element(col, row, value)

    return result