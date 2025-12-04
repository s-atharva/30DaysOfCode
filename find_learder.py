from typing import List


def find_leader(arr: List[int]) -> List[int]:
    leaders = []

    current_leader = arr[-1]
    leaders.append(current_leader)

    for i in range(len(arr) - 2, -1, -1):
        if arr[i] > current_leader:
            current_leader = arr[i]
            leaders.append(current_leader)

    return leaders[::-1]


my_arr = [10, 22, 12, 3, 0, 6]
print(find_leader(arr=my_arr))
