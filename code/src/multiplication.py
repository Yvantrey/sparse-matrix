from sparse_matrix import SparseMatrix, MatrixDimensionError

def multiply_matrices(matrix1, matrix2):
    if matrix1.cols != matrix2.rows:
        raise MatrixDimensionError(
            f"Invalid dimensions for multiplication: {matrix1.rows}x{matrix1.cols} and {matrix2.rows}x{matrix2.cols}. "
            f"First matrix columns ({matrix1.cols}) must match second matrix rows ({matrix2.rows})"
        )

    result = SparseMatrix(rows=matrix1.rows, cols=matrix2.cols)

    # Optimized multiplication directly using dictionary format
    for row in matrix1.data:
        row_data = {}  # Temporary storage for row results
        for k, v1 in matrix1.data[row].items():
            if k in matrix2.data:
                for col, v2 in matrix2.data[k].items():
                    row_data[col] = row_data.get(col, 0) + v1 * v2

        # Only store non-zero results
        for col, value in row_data.items():
            if value != 0:
                if row not in result.data:
                    result.data[row] = {}
                result.data[row][col] = value
                result.nnz += 1

    return result