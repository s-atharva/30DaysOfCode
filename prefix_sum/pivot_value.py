from typing import List


def find_pivot(arr: List[int]) -> int:
    n = len(arr)
    total = 0
    for elem in arr:
        total += elem
    left = 0
    for pivot in range(n):
        right = total - left - arr[pivot]
        if left == right:
            return pivot
        left += arr[pivot]
    return -1


def pivot_prefix_suffix(arr):
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]

    suffix = [0] * n
    suffix[n - 1] = arr[n - 1]

    for i in range(n):
        prefix[i] = prefix[i - 1] + arr[i]

    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] + arr[i]

    for i in range(n):
        if prefix[i] == suffix[i]:
            return i

    return -1


my_array = [-7, 1, 5, 2, -4, 3, 0]
print(find_pivot(arr=my_array))
# print(pivot_prefix_suffix(arr=my_array))
