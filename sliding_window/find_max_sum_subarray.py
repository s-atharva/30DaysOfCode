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


my_arr = [2, 3, 5, 2, 9, 7, 1]
print(find_max_sum(arr=my_arr, k=3))
