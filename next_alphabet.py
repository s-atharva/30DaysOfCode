from typing import List


def find_next_alphabet(arr: List[str], elem: str):
    start = 0
    end = len(arr) - 1
    next_alphabet = "Not Available"
    while start <= end:
        mid = (start + end) // 2
        if elem == arr[mid]:
            start = mid + 1
        elif elem <= arr[mid]:
            next_alphabet = arr[mid]
            end = mid - 1
        else:
            start = mid + 1
    return next_alphabet


my_arr = ['a', 'c', 'f', 'h']
elem = 'a'
print(find_next_alphabet(arr=my_arr, elem=elem))

