from sparse_matrix import SparseMatrix, MatrixDimensionError

def add_matrices(matrix1, matrix2):
    if (matrix1.rows, matrix1.cols) != (matrix2.rows, matrix2.cols):
        raise MatrixDimensionError(
            f"Cannot add matrices of different dimensions: "
            f"{matrix1.rows}x{matrix1.cols} and {matrix2.rows}x{matrix2.cols}"
        )

    result = SparseMatrix(rows=matrix1.rows, cols=matrix1.cols)

    # Add elements from matrix1
    for row in matrix1.data:
        for col, value in matrix1.data[row].items():
            result.set_element(row, col, value)

    # Add elements from matrix2
    for row in matrix2.data:
        for col, value in matrix2.data[row].items():
            current = result.get_element(row, col)
            result.set_element(row, col, current + value)

    return result