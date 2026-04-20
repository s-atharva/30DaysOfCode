def three_sum_problem(nums, target):
    nums.sort()
    lis = []
    for k in range(len(nums)):
        # skipping duplicate
        if k > 0 and nums[k] == nums[k - 1]:
            continue
        i = k + 1
        j = len(nums) - 1
        while i < j:
            total = nums[k] + nums[i] + nums[j]
            if total > target:
                j -= 1
            elif total < target:
                i += 1
            else:
                lis.append([nums[k], nums[i], nums[j]])
                i += 1
                j -= 1

                # skipping duplicate
                while i < j and nums[i] == nums[i - 1]:
                    i += 1
                while i < j and nums[i] == nums[i - 1]:
                    j += 1

    return lis


my_arr = [-1, 0, 1, 2, -1, 4]
print(three_sum_problem(nums=my_arr, target=0))
