from typing import List


def find_3_sum(arr: List[int]):
    n = len(arr)
    my_set = set()
    for i in range(0, n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    temp = list((arr[i], arr[j], arr[k]))
                    temp.sort()
                    my_set.add(tuple(temp))
    return [list(item) for item in my_set]


def find_3_sum_with_two_loops(arr: List[int]):
    n = len(arr)
    result = set()
    for i in range(0, n):
        my_set = set()
        for j in range(i + 1, n):
            third = -(arr[i] + arr[j])
            if third in my_set:
                temp = list((arr[i], arr[j], third))
                temp.sort()
                result.add(tuple(temp))
            else:
                my_set.add(arr[j])
    return [[item] for item in result]


my_arr = [-1, 0, 1, 2, -1, -4]
# print(find_3_sum(arr=my_arr))
print(find_3_sum_with_two_loops(arr=my_arr))
