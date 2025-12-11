from typing import List


def rotate_matrix_90(matrix: List[List[int]]) -> List[List[int]]:
    n = len(matrix)
    for i in range(0, n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
    return matrix


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(rotate_matrix_90(matrix=matrix))
