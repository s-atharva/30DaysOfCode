def two_sum(arr, target):
    nums = []
    n = len(arr)
    for i in range(n):
        nums.append((arr[i], i))

    nums.sort()

    left = 0
    right = n - 1

    while left < right:
        total = nums[left][0] + nums[right][0]
        if total == target:
            return [nums[left][1], nums[right][1]]
        elif total < target:
            left += 1
        else:
            right -= 1
    return []


my_arr = [3, 2, 4]
two_sum(arr=my_arr, target=6)
