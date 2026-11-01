def max_subarray_sum_k(arr, k):
    i, j = 0, 0
    total = 0
    maxi = 0
    while j < len(arr):
        total += arr[j]
        if j - i + 1 < k:
            j += 1
        elif j - i + 1 == k:
            maxi = max(maxi, total)
            total -= arr[i]
            i += 1
            j += 1
    return maxi


arr = [2, 5, 1, 8, 2, 9, 1]
k = 3
print(max_subarray_sum_k(arr, k))
