from typing import List


def find_elem_rotated_sorted_arr(arr: List[int], smallest_elem_index: int, elem: int) -> int:
    n = len(arr)
    check_elem_left = binary_search(arr=arr, start=0, end=smallest_elem_index - 1, elem=elem)
    if check_elem_left != -1:
        return check_elem_left
    return binary_search(arr=arr, start=smallest_elem_index, end=n - 1, elem=elem)


def binary_search(arr: List[int], start: int, end: int, elem: int) -> int:
    while start <= end:
        mid = (start + end) // 2
        if elem == arr[mid]:
            return mid
        elif elem < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def find_min_elem_array(arr: List[int]) -> int:
    length = len(arr)
    start = 0
    end = length - 1
    while start <= end:
        if arr[start] <= arr[end]:
            return start
        mid = (start + end) // 2
        prev = (mid - 1 + length) % length
        nxt = (mid + 1) % length
        if arr[prev] >= arr[mid] and arr[nxt] >= arr[mid]:
            return mid
        elif arr[start] < arr[mid]:
            start = mid + 1
        else:
            end = mid - 1


my_array = [11, 12, 15, 18, 2, 5, 6, 8]
min_elem_index = find_min_elem_array(arr=my_array)
# print(binary_search(arr=my_array, start=0, end=min_elem_index, elem=15))
# print(binary_search(arr=my_array, start=min_elem_index, end=len(my_array) - 1, elem=15))
print(f'Array = {my_array}')
print(f"Element = {15}")
print(find_elem_rotated_sorted_arr(arr=my_array, elem=15, smallest_elem_index=min_elem_index))
