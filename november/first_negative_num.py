from collections import deque


def find_first_negative_num(arr, k):
    result = []
    for i in range(len(arr) - k + 1):
        negative = 0
        for j in range(i, i + k):
            if arr[j] < 0:
                negative = arr[j]
                break
        result.append(negative)
    return result


def first_neg(arr, k):
    neg = deque()
    result = []
    i, j = 0, 0
    while j < len(arr):
        if arr[j] < 0:
            neg.append(arr[j])

        if j - i + 1 < k:
            j += 1

        elif j - i + 1 == k:
            if len(neg) == 0:
                result.append(0)

            else:
                if arr[i] == neg[0]:
                    elem = neg.popleft()
                    result.append(elem)
                    i += 1
                    j += 1
                else:
                    result.append(neg[0])
    return result


my_arr = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3
print(find_first_negative_num(my_arr, k))
