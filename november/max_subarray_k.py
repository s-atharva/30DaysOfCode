def max_subarray_k(arr, k):
    result = []
    n = len(arr)
    for i in range(n - k + 1):
        maxi = arr[i]
        for j in range(i + 1, i + k):
            if arr[j] > maxi:
                maxi = arr[j]

        result.append(maxi)
    return result


my_array = [1, 3, -1, -3, 5, 3, 6, 7]
window_size = 3
print(max_subarray_k(my_array, window_size))
