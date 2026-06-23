def find_nsl(arr):
    my_stack = []
    nsl = []
    for i in range(len(arr)):
        if len(my_stack) == 0:
            nsl.append(-1)
        elif len(my_stack) > 0 and my_stack[-1][0] < arr[i]:
            nsl.append(my_stack[-1][1])
        elif len(my_stack) > 0 and my_stack[-1][0] >= arr[i]:
            while len(my_stack) > 0 and my_stack[-1][0] >= arr[i]:
                my_stack.pop()
            if len(my_stack) == 0:
                nsl.append(-1)
            else:
                nsl.append(my_stack[-1][1])

        my_stack.append([arr[i], i])
    return nsl


def find_nsr(arr):
    my_stack = []
    nsr = []
    for i in range(len(arr) - 1, -1, -1):
        if len(my_stack) == 0:
            nsr.append(len(arr))
        elif len(my_stack) > 0 and my_stack[-1][0] < arr[i]:
            nsr.append(my_stack[-1][1])
        elif len(my_stack) > 0 and my_stack[-1][0] >= arr[i]:
            while len(my_stack) > 0 and my_stack[-1][0] >= arr[i]:
                my_stack.pop()
            if len(my_stack) == 0:
                nsr.append(len(arr))
            else:
                nsr.append(my_stack[-1][1])

        my_stack.append([arr[i], i])
    nsr.reverse()
    return nsr


def find_max_area_histogram(arr):
    nsl = find_nsl(arr)
    nsr = find_nsr(arr)
    width_arr = [-1] * len(arr)
    for i in range(len(arr)):
        width_arr[i] = nsr[i] - nsl[i] - 1
    print(width_arr)
    maxi = 0
    for i in range(len(arr)):
        elem = width_arr[i] * arr[i]
        maxi = max(maxi, elem)
    return maxi


def max_binary_rectangle(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    heights = [0] * cols
    max_area = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                heights[j] = 0
            else:
                heights[j] += 1
        max_area = max(max_area, find_max_area_histogram(heights))

    return max_area


my_arr = [
    [0, 1, 1, 0],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 0, 0]
]

# print(find_nsl(arr=my_arr))
# print(find_nsr(arr=my_arr))
# print(find_max_area_histogram(arr=my_arr))
print(max_binary_rectangle(matrix=my_arr))
