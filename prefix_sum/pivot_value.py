from typing import List


def find_pivot(arr: List[int]) -> int:
    n = len(arr)
    for i in range(n):
        left_sum = sum(arr[0:i])
        right_sum = sum(arr[i + 1:n])

        if left_sum == right_sum:
            return arr[i]
    return -1


my_array = [-7, 1, 5, 2, -4, 3, 0]
print(find_pivot(arr=my_array))
