def delete_middle(arr, k):
    if k == 1:
        arr.pop()
        return
    temp = arr.pop()
    delete_middle(arr, k - 1)
    arr.append(temp)


def solve(arr):
    if len(arr) == 0:
        return None
    k = len(arr) // 2 + 1
    delete_middle(arr, k=k)
    return arr


my_array = [1, 2, 3, 4, 5]
print(solve(my_array))
