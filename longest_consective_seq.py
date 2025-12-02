from typing import List


def find_longest_consecutive_seq(arr: List[int]) -> int:
    longest = 0
    pass
    for num in arr:
        current = num
        length = 1

        while (current + 1) in arr:
            current += 1
            length += 1

        longest = max(longest, length)

    return longest


my_arr = [102, 4, 100, 1, 101, 3, 2, 1, 1]
print(find_longest_consecutive_seq(arr=my_arr))
