def remove_duplicate(arr):
    unique_elements = list(set(arr))
    for i in range(len(unique_elements)):
        arr[i] = unique_elements[i]
    return arr


def remove_duplicate_two_pointers(arr):
    i = 0
    for j in range(i, len(arr)):
        if arr[j] != arr[i]:
            arr[i + 1] = arr[j]
            i += 1
    return arr


my_arr = [1, 1, 2, 2, 2, 3, 3]
print(remove_duplicate_two_pointers(my_arr))
