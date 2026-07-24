def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        # flag to check if any swaps were made
        swapped = False
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        # if no swap occurred, nums is already sorted
        if not swapped:
            break
    return nums


my_arr = [5, 6, 1, 3]
print(bubble_sort(nums=my_arr))
