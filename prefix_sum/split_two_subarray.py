def split_subarray(arr):
    n = len(arr)
    for i in range(n):
        left_sum = 0
        right_sum = 0

        for j in range(0, i + 1):
            left_sum += arr[j]

        for j in range(i + 1, n):
            right_sum += arr[j]

        if left_sum == right_sum:
            return True
    return False


def split_two_subarray(arr):
    total = sum(arr)
    left = 0
    for i in range(len(arr)):

        right = total - left
        print(left, right)
        if left == right:
            return True
        left += arr[i]

    return False


my_arr = [1, 2, 3, 4, 5, 5]
print(split_subarray(arr=my_arr))
print(split_two_subarray(arr=my_arr))
