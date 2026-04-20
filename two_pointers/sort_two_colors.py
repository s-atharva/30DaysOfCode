def sort_two_variable(nums):
    i = 0
    j = len(nums) - 1
    while i < j:
        if nums[i] == 0:
            i += 1
        elif nums[j] == 1:
            j -= 1
        else:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
    return nums


my_arr = [0, 1, 1, 1, 0, 0, 1, 1]
print(sort_two_variable(nums=my_arr))
