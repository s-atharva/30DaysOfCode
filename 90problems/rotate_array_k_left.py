def rotate_array_k_left(arr, k):
    n = len(arr)
    k = k % n

    temp = []
    for i in range(0, k):
        temp.append(arr[i])

    for i in range(k, n):
        arr[i - k] = arr[i]
    j = 0
    for i in range(n - k, n):
        arr[i] = temp[j]
        j += 1
    return arr


def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def reverse_left_k(arr, k):
    n = len(arr)
    k = k % n

    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)
    reverse(arr, 0, n - 1)

    return arr


my_array = [1, 2, 3, 4, 5, 6, 7]
# print(rotate_array_k_left(arr=my_array, k=3))
print(reverse_left_k(arr=my_array, k=3))
