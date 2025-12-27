def binary_search(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            # go to left side
            low = mid + 1
        else:
            # go to right side
            high = mid - 1
    return -1


def binary_search_recursive(nums, target, low, high):
    # base case: nums is empty
    if low > high:
        return -1
    mid = (low + high) // 2
    # base case: target found at mid
    if nums[mid] == target:
        return mid
    # recursive case
    elif target < nums[mid]:
        return binary_search_recursive(nums, target, low, mid - 1)
    else:
        return binary_search_recursive(nums, target, mid + 1, high)


arr = [2, 4, 6, 7, 9, 11, 18, 19]
target = 2
# print(binary_search(nums=arr, target=target))
print(binary_search_recursive(nums=arr, target=target, low=0, high=len(arr) - 1))
