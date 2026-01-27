def find_max_average(arr, k):
    i = 0
    j = 0
    max_average = 0
    total = 0
    while j < len(arr):
        total = total + arr[j]
        if j - i + 1 < k:
            j += 1
        elif j - i + 1 == k:
            max_average = max(max_average, total / k)
            total -= arr[i]
            i += 1
            j += 1
    return max_average


my_array = [2, 5, 1, 8, 2, 9, 1]
print(find_max_average(arr=my_array, k=3))
