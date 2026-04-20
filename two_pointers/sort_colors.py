def sort_colors(nums):
    count_0 = 0
    count_1 = 0
    count_2 = 0

    for elem in nums:
        if elem == 0:
            count_0 += 1
        elif elem == 1:
            count_1 += 1
        else:
            count_2 += 1

    # overwrite an array index
    index = 0
    for i in range(count_0):
        nums[index] = 0
        index += 1
    for i in range(count_1):
        nums[index] = 1
        index += 1
    for i in range(count_2):
        nums[index] = 2
        index += 1

    return nums

def sort_colors_two_pointers(nums):



my_array = [2, 0, 2, 1, 1, 0]
print(sort_colors(nums=my_array))
