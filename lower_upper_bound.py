from typing import List


def find_lower_bound(nums: List[int], target):
    n = len(nums)
    lower_bound = -1
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= target:
            lower_bound = mid
            high = mid - 1
        else:
            low = mid + 1
    return lower_bound


arr = [1, 1, 1, 2, 3, 3, 5, 6, 7, 7, 7, 9, 12, 12, 13]
print(find_lower_bound(nums=arr, target=9))
