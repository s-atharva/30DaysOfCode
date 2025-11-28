from typing import List


def rearrange_elem_by_sign(arr: List[int]) -> List[int]:
    # T.C. -> O(n)
    # S.C. -> O(n)
    print(arr)
    positive_elem = []
    negative_elem = []
    for i in range(len(arr)):
        if arr[i] > 0:
            positive_elem.append(arr[i])
        else:
            negative_elem.append(arr[i])
    for i in range(len(arr) // 2):
        arr[2 * i] = positive_elem[i]
        arr[2 * i + 1] = negative_elem[i]
    return arr


my_array = [3, 1, - 2, -5, 2, -4]
print(rearrange_elem_by_sign(arr=my_array))
