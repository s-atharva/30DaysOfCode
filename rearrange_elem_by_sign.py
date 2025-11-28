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


def rearrange_elem_by_sign_optimal(arr: List[int]) -> List[int]:
    result = [0] * len(arr)
    positive = 0
    negative = 1

    for i in range(len(arr)):
        if arr[i] > 0:
            result[positive] = arr[i]
            positive += 2
        else:
            result[negative] = arr[i]
            negative += 2
    return result


def rearrange_elem_by_sign_version_2(arr: List[int]) -> List[int]:
    result = [0] * len(arr)
    positive_arr = []
    negative_arr = []
    for elem in arr:
        if elem > 0:
            positive_arr.append(elem)
        else:
            negative_arr.append(elem)
    if len(positive_arr) > len(negative_arr):
        for i in range(0, len(negative_arr)):
            result[2 * i] = positive_arr[i]
            result[2 * i + 1] = negative_arr[i]
        for i in range(len(negative_arr), len(positive_arr)):
            result[len(negative_arr) * 2] = positive_arr[i]
    else:
        for i in range(0, len(positive_arr)):
            result[2 * i] = positive_arr[i]
            result[2 * i + 1] = negative_arr[i]
        for i in range(len(negative_arr), len(positive_arr)):
            result[len(positive_arr) * 2] = negative_arr[i]

    return result


def rearrange_elem_version_2(arr: List[int]) -> List[int]:
    result = []
    positive_arr = []
    negative_arr = []
    for elem in arr:
        if elem > 0:
            positive_arr.append(elem)
        else:
            negative_arr.append(elem)
    print(positive_arr)
    print(negative_arr)

    i = 0
    while i < len(positive_arr) and i < len(negative_arr):
        result.append(positive_arr[i])
        result.append(negative_arr[i])
        i += 1

    while i < len(positive_arr):
        result.append(positive_arr[i])
        i += 1

    while i < len(negative_arr):
        result.append(negative_arr[i])
        i += 1

    return result


my_array = [-1, 2, 3, 4, -3, 1]
# print(rearrange_elem_by_sign(arr=my_array))
# print(rearrange_elem_by_sign_optimal(arr=my_array))
# print(rearrange_elem_by_sign_version_2(arr=my_array))
print(rearrange_elem_version_2(arr=my_array))
