from typing import List


def find_pivot(arr: List[int]) -> int:
    n = len(arr)
    for i in range(n):
        left_sum = 0
        for left_index in range(0, i):
            left_sum += arr[left_index]

        right_sum = 0
        for right_index in range(i + 1, n):
            right_sum += arr[right_index]

        if left_sum == right_sum:
            return arr[i]
    return -1


my_array = [-7, 1, 5, 2, -4, 3, 0]
print(find_pivot(arr=my_array))
