from typing import List


def find_min_difference(arr: List[int], elem: int) -> int:
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if elem == arr[mid]:
            return mid
        elif elem <= arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return end


my_arr = [1, 3, 8, 10, 15]
target = 9
print(find_min_difference(arr=my_arr, elem=target))
