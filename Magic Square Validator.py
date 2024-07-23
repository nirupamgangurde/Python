def is_magic_square(matrix):
    n = len(matrix)
    magic_sum = sum(matrix[0])

    for i in range(n):
        if sum(matrix[i]) != magic_sum or sum(row[i] for row in matrix) != magic_sum:
            return False

    # Check diagonals
    if sum(matrix[i][i] for i in range(n)) != magic_sum or sum(matrix[i][n - 1 - i] for i in range(n)) != magic_sum:
        return False

    return True

matrix = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

print(is_magic_square(matrix))
