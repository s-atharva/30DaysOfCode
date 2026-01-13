from typing import List


def find_ceil_elem(arr: List[int], elem: int) -> int:
    start = 0
    end = len(arr) - 1
    large = -1
    while start <= end:
        mid = (start + end) // 2
        if elem == arr[mid]:
            return arr[mid]
        elif elem < arr[mid]:
            large = arr[mid]
            end = mid - 1
        else:
            start = mid + 1
    return large


my_arr = [1, 2, 3, 4, 8, 10, 10, 12, 19]
print(find_ceil_elem(arr=my_arr, elem=15))
