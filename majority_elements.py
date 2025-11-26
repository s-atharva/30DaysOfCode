from typing import List


def find_majority_elem(arr: List[int]) -> int:
    for i in range(0, len(arr)):
        count = 0
        for j in range(0, len(arr)):
            if arr[i] == arr[j]:
                count += 1
        if count > len(arr) / 2:
            return count
    # no majority elements
    return -1


def find_majority_elem_dictionary(arr: List[int]) -> int:
    # time complexity = O(n) + O(n) = 2*O(n) = O(n)
    # space complexity = O(n)
    elem_count = dict()
    # O(n)
    for elem in arr:
        if elem not in elem_count:
            elem_count[elem] = 1
        else:
            elem_count[elem] += 1
    # O(n)
    for key in elem_count:
        if elem_count[key] > len(arr) // 2:
            return key
    return -1


def find_majority_elem_moore_voting_algo(arr: List[int]) -> int:
    # T.C = O(n)
    # if array is empty
    if len(arr) == 0:
        return -1
    elem = 0
    count = 0
    for num in arr:
        if count == 0:
            elem = num
        if num == elem:
            count += 1
        else:
            count -= 1
    print(elem, count)
    # verification step
    if arr.count(elem) > len(arr) // 2:
        return elem
    # no majority elem present
    return -1


my_arr = [7, 7, 5, 7, 5, 1, 5, 7, 7, 5, 5, 7, 7, 5, 5, 5, 5]
# print(find_majority_elem(arr=my_arr))
# print(find_majority_elem_dictionary(arr=my_arr))
print(find_majority_elem_moore_voting_algo(arr=my_arr))
