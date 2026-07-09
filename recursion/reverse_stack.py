# def reverse_stack_loop(arr):
#     reversed_arr = []
#     while len(arr) > 0:
#         reversed_arr.append(arr.pop())
#     return reversed_arr


def reverse_stack(arr, reversed_arr):
    if len(arr) == 0:
        return None
    # pop last elem
    temp = arr.pop()
    # induction step
    reversed_arr.append(temp)
    # hypothesis
    reverse_stack(arr, reversed_arr)


def reverse_stack_without_space(arr):
    if len(arr) == 1:
        return None
    temp = arr.pop()
    reverse_stack_without_space(arr)
    insert_front(arr, temp)


def insert_front(arr, temp):
    if len(arr) == 0:
        arr.append(temp)
        return None
    val = arr.pop()
    insert_front(arr, temp)
    arr.append(val)


my_arr = [1, 2, 3, 4, 5]
reversed_arr = []
# print(reverse_stack_loop(my_arr))
# reverse_stack(my_arr, reversed_arr)
reverse_stack_without_space(my_arr)
print(my_arr)
# print(reversed_arr)
