from typing import List


def find_long_consecutive_seq_brute(arr: List[int]) -> int:
    largest = 0
    for elem in arr:
        current = elem
        current_count = 1
        while current + 1 in arr:
            current += 1
            current_count += 1
        largest = max(largest, current_count)
    return largest


def find_long_consecutive_seq_better(arr: List[int]) -> int:
    if not arr:
        return 0
    # sort arr
    arr.sort()

    largest = 1
    current_count = 0
    last_smaller = -1

    for i in range(len(arr)):
        if arr[i] - 1 == last_smaller:
            current_count += 1
            last_smaller = arr[i]
        elif arr[i] != last_smaller:
            current_count = 1
            last_smaller = arr[i]
        largest = max(largest, current_count)
    return largest


def find_long_consecutive_seq_set(arr: List[int]) -> int:
    my_set = set()
    for elem in arr:
        my_set.add(elem)

    largest = 0
    for num in my_set:
        if num - 1 not in my_set:
            current = num
            current_count = 1
            while current + 1 in my_set:
                current_count += 1
                current += 1
            largest = max(largest, current_count)
    return largest


my_arr = [102, 4, 100, 1, 102, 3, 2, 1, 1]
print(find_long_consecutive_seq_brute(arr=my_arr))
print(find_long_consecutive_seq_better(arr=my_arr))
print(find_long_consecutive_seq_set(arr=my_arr))
