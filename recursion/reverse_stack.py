def reverse_stack(arr):
    # base case
    if len(arr) == 1:
        return None
    temp = arr.pop()
    reverse_stack(arr)
    arr.append(temp)


my_arr = [5, 4, 3, 2, 1]
print(my_arr)
reverse_stack(my_arr)
print(my_arr)
