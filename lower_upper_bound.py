from typing import List


def find_lower_bound(nums: List[int], target):
    start = 0
    end = len(nums) - 1
    lower_bound = -1
    while start <= end:
        mid = (start + end) // 2
        if target == arr[mid]:
            lower_bound = mid
            end = mid - 1
        elif target <= arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return lower_bound


def find_upper_bound(nums: List[int], target):
    start = 0
    end = len(nums) - 1
    upper_bound = -1
    while start <= end:
        mid = (start + end) // 2
        if target == nums[mid]:
            upper_bound = mid
            start = mid + 1
        elif target <= nums[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return upper_bound


arr = [1, 1, 1, 2, 3, 3, 5, 6, 7, 7, 7, 9, 12, 12, 13]
lower = find_lower_bound(nums=arr, target=7)
higher = find_upper_bound(nums=arr, target=7)
print(higher - lower + 1)
