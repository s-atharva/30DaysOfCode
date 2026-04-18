def merge_two_sorted_array(nums1, nums2, m, n):
    k = len(nums1) - 1
    for i in range(0, n):
        nums1[k] = nums2[i]
        k -= 1
    return sorted(nums1)


def merge_two_sorted_arr_two_pointers(nums1, nums2, m, n):
    i = m - 1
    j = n - 1
    k = m + n - 1
    while j >= 0:
        if nums1[i] > nums2[j] and i >= 0:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    return nums1


nums_arr_1 = [1, 2, 3, 0, 0, 0]
nums_arr_2 = [2, 5, 6]
# print(merge_two_sorted_array(nums1=nums_arr_1, nums2=nums_arr_2, m=3, n=3))
print(merge_two_sorted_arr_two_pointers(nums1=nums_arr_1, nums2=nums_arr_2, m=3, n=3))
