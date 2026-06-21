def nle(arr):
    my_stack = []
    result = []
    for i in range(len(arr) - 1, -1, -1):
        if len(my_stack) == 0:
            result.append(-1)
        elif len(my_stack) > 0 and my_stack[-1] > arr[i]:
            result.append(my_stack[-1])
        elif len(my_stack) > 0 and my_stack[-1] <= arr[i]:
            while len(my_stack) > 0 and my_stack[-1] <= arr[i]:
                my_stack.pop()
            if my_stack[-1] > arr[i]:
                result.append(my_stack[-1])
            else:
                result.append(-1)
        my_stack.append(arr[i])
    result.reverse()
    return result


my_arr = [1, 3, 2, 4]
print(nle(arr=my_arr))
