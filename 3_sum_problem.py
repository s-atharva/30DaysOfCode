from typing import List


def find_3_sum(arr: List[int]) -> List[tuple]:
    n = len(arr)
    my_set = set()
    for i in range(0, n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    temp = [arr[i], arr[j], arr[k]]
                    temp.sort()
                    my_set.add(tuple(temp))
    return list(my_set)


def find_3_sum_2_approach(arr: List[int]) -> list[tuple]:
    n = len(arr)
    result = set()
    for i in range(0, n):
        my_set = set()
        for j in range(i + 1, n):
            third = -(arr[i] + arr[j])
            if third in my_set:
                temp = [arr[i], arr[j], third]
                temp.sort()
                result.add(tuple(temp))
            my_set.add(arr[j])
    return list(result)


my_arr = [-1, 0, 1, 2, -1, 4]
print(find_3_sum(arr=my_arr))
print(find_3_sum_2_approach(arr=my_arr))
