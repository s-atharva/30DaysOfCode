from typing import List


def find_max_sum(arr: List[int], k) -> int:
    max_sum = -1
    n = len(arr)
    for i in range(0, n - k + 1):
        current_sum = 0
        for j in range(i, i + k):
            current_sum += arr[j]
        max_sum = max(max_sum, current_sum)
    return max_sum


def find_max_sum_bs(arr: List[int], k) -> int:
    total = 0
    max_total = 0
    i, j = 0, 0
    while j < len(arr):
        total = total + arr[j]
        if j - i + 1 < k:
            j += 1
        elif j - i + 1 == k:
            max_total = max(total, max_total)
            total = total - arr[i]
            i += 1
            j += 1
    return max_total


my_arr = [2, 3, 5, 2, 9, 7, 1]
print(find_max_sum(arr=my_arr, k=3))
print(find_max_sum_bs(arr=my_arr, k=3))
