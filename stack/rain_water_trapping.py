def rain_water_trapping(arr):
    n = len(arr)
    left_max = []
    right_max = []

    for i in range(n):
        max_val = 0
        for j in range(i - 1, -1, -1):
            if arr[j] > max_val:
                max_val = arr[j]
        left_max.append(max_val)

    for i in range(n):
        max_val = 0
        for j in range(i + 1, n):
            if arr[j] > max_val:
                max_val = arr[j]
        right_max.append(max_val)

    print(left_max)
    print(right_max)
    water_level = []
    for i in range(n):
        level = min(left_max[i], right_max[i]) - arr[i]
        if level < 0:
            water_level.append(0)
        else:
            water_level.append(level)
    print(sum(water_level))


def trap(height):
    n = len(height)

    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])

    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    water = 0
    for i in range(n):
        water += min(left_max[i], right_max[i]) - height[i]

    return water


my_arr = [3, 0, 0, 2, 0, 4]
rain_water_trapping(arr=my_arr)
print(trap(height=my_arr))
