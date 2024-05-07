#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by given number.

    Parameters:
        matrix (list of lists): Matrix of integers or  floats.
        div (int or float): Number to divide the elements of the matrix

    Returns:
    list of lists: New matrix with elements.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats
        ZeroDivisionError: If div is equal to 0.
        TypeError: If each row of the matrix does not have the same size
    """
    if not isinstance(matrix, list) or \
      not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    row_sizes = set(len(row) for row in matrix)
    if len(row_sizes) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return new_matrix
