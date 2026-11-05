def longest_subarray_sum(arr, k):
    i, j = 0, 0
    sum = 0
    max_len = 0
    n = len(arr)

    while j < n:
        sum += arr[j]

        if sum < k:
            j += 1

        elif sum == k:
            max_len = max(max_len, j - i + 1)
            j += 1

        elif sum > k:
            while sum > k:
                sum -= arr[i]
                i += 1

            if sum == k:
                max_len = max(max_len, j - i + 1)

            j += 1
    return max_len


my_array = [4, 1, 1, 1, 2, 3, 5]
total = 5
print(longest_subarray_sum(my_array, total))
