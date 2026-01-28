from typing import List


def find_first_negative_number(arr: List[int], k: int) -> List[int]:
    negative_list = []
    n = len(arr)
    for i in range(0, n - k + 1):
        found = False
        for j in range(i, i + k):
            if arr[j] < 0:
                negative_list.append(arr[j])
                found = True
                break
        if not found:
            negative_list.append(0)
    return negative_list


my_arr = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3
print(find_first_negative_number(arr=my_arr, k=k))
