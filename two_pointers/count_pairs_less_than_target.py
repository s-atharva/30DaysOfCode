def count_pairs(nums, target):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] < target:
                count += 1
    return count


def count_pairs_tp(nums, target):
    count = 0
    nums.sort()
    i = 0
    j = len(nums) - 1
    while i < j:
        total = nums[i] + nums[j]
        if total < target:
            count += (j - i)
            i += 1
        else:
            j -= 1
    return count


nums = [-1, 1, 2, 3, 1]
target = 2
print(count_pairs(nums, target))
print(count_pairs_tp(nums, target))
