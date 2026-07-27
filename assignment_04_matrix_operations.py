# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(rows, cols, name="Matrix"):
    """Read a matrix of given size from the user, one row per line."""
    print(f"\nEnter {name} ({rows}x{cols}):")
    matrix = []
    for i in range(rows):
        row = input(f"Enter row {i + 1}: ").split()
        row = [float(x) for x in row]
        matrix.append(row)
    return matrix


def display_matrix(matrix):
    """Display a matrix in a neat, aligned grid format."""
    for row in matrix:
        formatted_row = "  ".join(f"{val:g}" for val in row)
        print(formatted_row)


def transpose_matrix(matrix):
    """Return the transpose of a matrix (rows become columns)."""
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result


def add_matrices(matrix_a, matrix_b):
    """Return the element-wise sum of two same-sized matrices."""
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    result = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]

    return result


def multiply_matrices(matrix_a, matrix_b):
    """Return the matrix product of A (MxN) and B (NxP)."""
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

    result = [[0] * cols_b for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += matrix_a[i][k] * matrix_b[k][j]
            result[i][j] = total

    return result


def main():
    # ---------------- Part A: Transpose ----------------
    print("=== Part A: Transpose a Matrix ===")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = read_matrix(rows, cols, "Matrix")

    print("\nOriginal Matrix:")
    display_matrix(matrix)

    transposed = transpose_matrix(matrix)
    print("\nTransposed Matrix:")
    display_matrix(transposed)

    # ---------------- Part B: Addition ----------------
    print("\n=== Part B: Add Two Matrices ===")
    rows_b = int(input("Enter number of rows: "))
    cols_b = int(input("Enter number of columns: "))
    matrix_a1 = read_matrix(rows_b, cols_b, "Matrix A")
    matrix_a2 = read_matrix(rows_b, cols_b, "Matrix B")

    sum_matrix = add_matrices(matrix_a1, matrix_a2)
    print("\nSum of Matrices:")
    display_matrix(sum_matrix)

    # ---------------- Part C: Multiplication ----------------
    print("\n=== Part C: Multiply Two Matrices ===")
    rows_m = int(input("Enter rows for Matrix A: "))
    cols_m = int(input("Enter columns for Matrix A (= rows for Matrix B): "))
    cols_n = int(input("Enter columns for Matrix B: "))

    matrix_m1 = read_matrix(rows_m, cols_m, "Matrix A")
    matrix_m2 = read_matrix(cols_m, cols_n, "Matrix B")

    product = multiply_matrices(matrix_m1, matrix_m2)
    print("\nProduct Matrix:")
    display_matrix(product)


if __name__ == "__main__":
    main()

