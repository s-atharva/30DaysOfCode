def find_elem_in_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    rows = len(matrix)
    cols = len(matrix[0])

    i = 0
    j = cols - 1

    while i < rows and j >= 0:
        if matrix[i][j] == target:
            return True
        elif target > matrix[i][j]:
            i += 1
        else:
            j -= 1
    return False


my_matrix = [[10, 20, 30, 40],
             [15, 25, 35, 45],
             [27, 29, 37, 48]]

print(find_elem_in_matrix(matrix=my_matrix, target=7))
