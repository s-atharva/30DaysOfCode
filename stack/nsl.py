def nsl(arr):
    my_stack = []
    result = []
    for i in range(len(arr)):
        if len(my_stack) == 0:
            result.append(-1)
        elif len(my_stack) > 0 and my_stack[-1] < arr[i]:
            result.append(my_stack[-1])
        elif len(my_stack) > 0 and my_stack[-1] >= arr[i]:
            while len(my_stack) > 0 and my_stack[-1] >= arr[i]:
                my_stack.pop()
            if len(my_stack) == 0:
                result.append(-1)
            else:
                result.append(my_stack[-1])
        my_stack.append(arr[i])
    return result


my_arr = [4, 5, 2, 10, 8]
print(nsl(arr=my_arr))
