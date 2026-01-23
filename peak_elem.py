from typing import List


def peakIndexInMountainArray(arr: List[int]) -> int:
    n = len(arr)
    # only one element
    if n == 1:
        return 0
    start = 0
    end = n - 1
    while start <= end:
        mid = start + (end - start) // 2
        if mid > 0 and mid < n - 1:
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid] > arr[mid - 1]:
                start = mid + 1
            else:
                end = mid - 1

        # first elem is at peak
        elif mid == 0:
            if arr[0] > arr[1]:
                return 0
            else:
                return 1

        # last elem is at peak
        elif mid == n - 1:
            if arr[n - 1] > arr[n - 2]:
                return n - 1
            else:
                return n - 2


arr = [0, 12, 6, 2]
print(peakIndexInMountainArray(arr=arr))
