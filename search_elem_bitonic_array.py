from typing import List


def peak_elem(arr: List[int]) -> int:
    n = len(arr)
    # only one elem present
    if n == 1:
        return 0
    start = 0
    end = n - 1
    while start <= end:
        mid = start + (end - start) // 2
        if 0 < mid < n - 1:
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid] > arr[mid - 1]:
                start = mid + 1
            else:
                end = mid - 1
        elif mid == 0:
            if arr[0] > arr[1]:
                return 0
            else:
                return 1
        elif mid == n - 1:
            if arr[n - 1] > arr[n - 2]:
                return n - 1
            else:
                return n - 2


def increasing_binary_search(arr: List[int], start, end, element) -> int:
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == element:
            return mid
        elif element < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def decreasing_binary_search(arr: List[int], start, end, element) -> int:
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == element:
            return mid
        elif element < arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1


my_arr = [1, 3, 8, 12, 4, 2]
peak_element = peak_elem(arr=my_arr)
find_elem = increasing_binary_search(arr=my_arr, start=0, end=peak_element + 1, element=4)

if find_elem == -1:
    find_elem = decreasing_binary_search(arr=my_arr, start=peak_element, end=len(my_arr), element=4)

print(find_elem)
