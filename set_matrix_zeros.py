from typing import List


def set_martix_zeros(nums: List[List[int]]):
    rows = len(nums)
    cols = len(nums[0])
    zeros_place = []
    for i in range(0, rows):
        for j in range(0, cols):
            if nums[i][j] == 0:
                zeros_place.append([i, j])
    for zero in zeros_place:
        for i in range(0, rows):
            nums[i][zero[1]] = 0
        for j in range(0, cols):
            nums[zero[0]][j] = 0
    return nums


def print_matrix(num: List[List[int]]):
    for i in range(len(num)):
        for j in range(len(num[0])):
            print(num[i][j], end=" ")
        print()


matrix = [[7, 9, 2, 3],
          [20, 8, 0, 10],
          [29, 0, -10, 5],
          [4, 14, 6, 7]]
set_matrix = set_martix_zeros(nums=matrix)
print_matrix(set_matrix)