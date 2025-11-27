from typing import List


def max_subarray_sum(arr: List[int]) -> int:
    # T.C. = O(n)
    # S.C. = O(1)
    maximum = float('-inf')
    total = 0
    for i in range(0, len(arr)):
        total = total + arr[i]
        if total <= 0:
            total = 0
        if total > maximum:
            maximum = total
    return maximum


def print_max_subarray_sum(arr: List[int]) -> int:
    maximum = float('-inf')
    total = 0
    ans_start = 0
    ans_end = 0
    start = 0
    for i in range(0, len(arr)):
        total = total + arr[i]

        if total < 0:
            total = 0
            start = i + 1

        if total > maximum:
            maximum = total
            ans_start = start
            ans_end = i + 1
    print(arr[ans_start:ans_end])
    return maximum


my_array = [-2, -3, 4, -1, -2, 1, 5, -3]
# my_array = [-1, -2, -3, -4]
# print(max_subarray_sum(arr=my_array))
print(print_max_subarray_sum(arr=my_array))
