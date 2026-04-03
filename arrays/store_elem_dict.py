my_dict = dict()
nums = [5, 6, 7, 7, 1, 9, 111, 1, 5, 1, 1]
for i in range(len(nums)):
    if nums[i] not in my_dict:
        my_dict[nums[i]] = 1
    else:
        my_dict[nums[i]] += 1

print(my_dict)
