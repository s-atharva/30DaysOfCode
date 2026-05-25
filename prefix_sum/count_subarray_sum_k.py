def count_subarray(arr, k):
    count = 0
    n = len(arr)
    for i in range(0, n):
        total = 0
        for j in range(i, n):
            total += arr[j]
            if total == k:
                count += 1

    return count


my_arr = [1, 2, 3, 4]
print(count_subarray(arr=my_arr, k=5))
