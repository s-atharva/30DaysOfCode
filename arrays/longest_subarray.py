def find_longest_subarray(arr, k):
    n = len(arr)
    max_total = 0
    for i in range(0, n - k + 1):
        total = 0
        for j in range(i, i + k):
            total += arr[j]
        max_total = max(max_total, total)
    return max_total


my_arr = [1, 2, 3, 1, 1, 1, 1, 4, 2, 3]
print(find_longest_subarray(arr=my_arr, k=3))
