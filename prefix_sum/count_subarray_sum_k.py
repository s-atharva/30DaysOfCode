def count_subarray(arr, k):
    prefix_sum = 0
    count = 0

    frequency = {0: 1}

    for num in arr:
        prefix_sum += num
        need = prefix_sum - k

        if need in frequency:
            count += frequency[need]

        if prefix_sum not in frequency:
            frequency[prefix_sum] = 1
        else:
            frequency[prefix_sum] += 1
    return count


my_arr = [1, 2, 3, -3, 1, 1, 1]
print(count_subarray(arr=my_arr, k=3))
