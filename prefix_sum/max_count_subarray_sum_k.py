def max_count_subarray(arr, k):
    maxi = 0
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            total = 0
            for index in range(i, j + 1):
                total += arr[index]

            if total == k:
                maxi = max(maxi, j - i + 1)
    return maxi


my_arr = [1, 2, 3, 1, 1, 1, 1]
print(max_count_subarray(arr=my_arr, k=4))
