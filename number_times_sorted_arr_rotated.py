from typing import List


def find_sorted_times(arr: List[int]) -> int:
    n = len(arr)
    start = 0
    end = n - 1
    while start <= end:
        # if array is sorted
        if arr[start] <= arr[end]:
            return start
        # if array is not sorted
        mid = (start + end) // 2
        prev = (mid - 1 + n) % n
        nxt = (mid + 1) % n
        if arr[prev] > arr[mid] and arr[nxt] > arr[mid]:
            return mid
        if arr[start] < arr[mid]:
            start = mid + 1
        else:
            end = mid - 1


my_list = [11, 12, 15, 18, 2, 5, 6, 8]
print(find_sorted_times(arr=my_list))
