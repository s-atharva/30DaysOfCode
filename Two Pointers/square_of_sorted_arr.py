def square_sorted_arr(s):
    left = 0
    n = len(s)
    right = n - 1
    temp = [0] * n
    k = n - 1

    while left < right:
        if abs(s[left]) < abs(s[right]):
            temp[k] = s[right] ** 2
            right -= 1
        else:
            temp[k] = s[left] ** 2
            left += 1

        k -= 1
    return temp


s = [-4, -1, 0, 3, 10]
print(square_sorted_arr(s))
