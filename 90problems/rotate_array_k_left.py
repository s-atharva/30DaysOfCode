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


my_array = [1, 2, 3, 4, 5, 6, 7]
print(rotate_array_k_left(arr=my_array, k=13))
