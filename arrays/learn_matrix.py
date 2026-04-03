from typing import List


def print_matrix(nums: List[List[int]]):
    rows = len(nums)
    column = len(nums[0])
    for i in range(0, rows):
        for j in range(0, column):
            print(nums[i][j], end=" ")
        print()


def print_upper_triangular_matrix(nums: List[List[int]]):
    rows = len(nums)
    cols = len(nums[0])
    for i in range(0, rows):
        for j in range(0, cols):
            if i <= j:
                print(nums[i][j], end="")
            else:
                print('*', end="")
            if j < cols - 1:
                print(" ", end="")
        print()


def print_lower_triangular_matrix(nums: List[List[int]]):
    rows = len(nums)
    cols = len(nums[0])
    for i in range(0, rows):
        for j in range(0, cols):
            if i >= j:
                print(nums[i][j], end="")
            else:
                print("*", end="")
            if j < cols - 1:
                print(" ", end="")
        print()


arr_matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

# print_matrix(nums=arr_matrix)
# print_upper_triangular_matrix(nums=arr_matrix)
print_lower_triangular_matrix(nums=arr_matrix)
