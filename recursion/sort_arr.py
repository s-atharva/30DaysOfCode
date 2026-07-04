def sort_arr(arr):
    if len(arr) == 1:
        return
    temp = arr.pop()
    sort_arr(arr)
    insert_temp(arr, temp)


def insert_temp(arr, temp):
    if len(arr) == 0 or arr[-1] <= temp:
        arr.append(temp)
        return
    val = arr.pop()
    insert_temp(arr, temp)
    arr.append(val)


my_arr = [1, 0, 5, 2]
sort_arr(my_arr)
print(my_arr)
