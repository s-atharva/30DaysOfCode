from typing import List
from collections import deque


def find_max_all_window(arr: List[int], k: int) -> List[int]:
    answer = []
    n = len(arr)
    for i in range(0, n - k + 1):
        temp_max = float('-inf')
        for j in range(i, i + k):
            if arr[j] > temp_max:
                temp_max = arr[j]
        answer.append(temp_max)
    return answer


def find_max_all_window_sliding_window(arr: List[int], k: int) -> List[int]:
    i, j = 0, 0
    dq = deque()
    ans = []
    while j < len(arr):
        while dq and dq[-1] < arr[j]:
            dq.pop()

        dq.append(arr[j])

        if j - i + 1 < k:
            j += 1

        if j - i + 1 == k:
            ans.append(dq[0])
            if arr[i] == dq[0]:
                dq.popleft()
            i += 1
            j += 1
    return ans


my_arr = [1, 3, -1, -3, 5, 3, 6, 7]
window_size = 3
# print(find_max_all_window(arr=my_arr, k=window_size))
print(find_max_all_window_sliding_window(arr=my_arr, k=window_size))
