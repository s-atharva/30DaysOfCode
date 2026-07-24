def selection_sort(nums):
    for i in range(len(nums)):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


my_arr = [5, 7, 8, 4, 1, 6, 9, 2]
print(selection_sort(my_arr))
