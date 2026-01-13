from typing import List


def find_floor(arr: List[int], elem: int):
    n = len(arr)
    start = 0
    end = n - 1
    larger = -1
    while start <= end:
        mid = (start + end) // 2
        if elem == arr[mid]:
            return arr[mid]
        elif elem < arr[mid]:
            end = mid - 1
        else:
            larger = max(larger, arr[mid])
            start = mid + 1
    return larger


my_arr = [1, 2, 3, 4, 8, 10, 10, 12, 19]
print(find_floor(arr=my_arr, elem=5))
