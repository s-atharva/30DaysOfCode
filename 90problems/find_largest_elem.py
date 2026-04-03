def find_largest_element(my_array):
    largest = my_array[0]
    for elem in my_array:
        if elem > largest:
            largest = elem
    return largest


def find_second_largest(my_array):
    my_array.sort()
    largest = my_array[-1]
    for i in range(len(my_array) - 2, -1, -1):
        if my_array[i] < largest:
            return my_array[i]
    return 'Not Found'


def find_second_largest_two_loops(my_array):
    largest = -1
    second_largest = -1
    for i in range(len(my_array)):
        if my_array[i] > largest:
            largest = my_array[i]
    for i in range(len(my_array)):
        if my_array[i] > second_largest:
            if my_array[i] < largest:
                second_largest = my_array[i]
    return second_largest


def find_second_largest_n(my_array):
    largest = my_array[0]
    slargest = -1
    for i in range(1, len(my_array)):
        if my_array[i] > largest:
            slargest = largest
            largest = my_array[i]
        elif my_array[i] > slargest and my_array[i] != largest:
            slargest = my_array[i]
    return slargest


my_arr = [1, 2, 4, 7, 7, 5]
print(find_largest_element(my_arr))
print(find_second_largest(my_arr))
print(find_second_largest_two_loops(my_arr))
print(find_second_largest_n(my_arr))
