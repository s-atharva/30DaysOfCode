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


def find_first_negative_number_sliding_window(arr, k):
    i, j = 0, 0
    n = len(arr)
    first_negative = list()
    temp_nagative = list()
    while j < n:
        if arr[j] < 0:
            temp_nagative.append(arr[j])
        if j - i + 1 < k:
            j += 1
        elif j - i + 1 == k:
            if len(temp_nagative) == 0:
                first_negative.append(0)
            else:
                first_negative.append(temp_nagative[0])
                if arr[i] < 0:
                    temp_nagative.pop(0)
            i += 1
            j += 1
    return first_negative


my_arr = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3
print(find_first_negative_number(arr=my_arr, k=k))
print(find_first_negative_number_sliding_window(arr=my_arr, k=k))
