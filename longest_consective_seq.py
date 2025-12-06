from typing import List


def find_long_consecutive_seq_brute(arr: List[int]) -> int:
    longest = 0
    for elem in arr:
        current = elem
        current_count = 1
        while current + 1 in arr:
            current += 1
            current_count += 1
        longest = max(longest, current_count)

    return longest


my_arr = [102, 4, 100, 1, 102, 3, 2, 1, 1]
print(find_long_consecutive_seq_brute(arr=my_arr))
