from typing import List


def find_sorted_times(arr: List[int]) -> int:
    start = 0
    end = len(arr) - 1
    n = len(arr)
    # if sorted
    while start <= end:
        if arr[start] <= arr[end]:
            return start

        mid = (start + end) // 2
        prev = (mid - 1 + n) % n
        next = (mid + 1) % n

        if arr[mid] <= arr[prev] and arr[mid] <= arr[next]:
            return mid

        if arr[mid] >= arr[start]:
            start = mid + 1
        else:
            end = mid - 1


my_list = [11, 12, 15, 18, 2, 5, 6, 8]
print(find_sorted_times(arr=my_list))

