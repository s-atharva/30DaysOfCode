from typing import List


def find_lower_bound(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    lower_bound = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            lower_bound = mid
            high = mid - 1
        elif target <= nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return lower_bound


def find_upper_bound(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    upper_bound = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            upper_bound = mid
            low = mid + 1
        elif target <= nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return upper_bound


nums_list = [2, 4, 10, 10, 10, 18, 20]
print(find_lower_bound(nums=nums_list, target=10))
print(find_upper_bound(nums=nums_list, target=10))
