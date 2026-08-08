def two_sum(arr, target):
    # for i in range(len(arr)):
    #     for j in range(i + 1, len(arr)):
    #         if arr[i] + arr[j] == target:
    #             return [i, j]
    # return []

    # TC -> O(n) and SC -> O(n)
    my_dict = {}
    for i in range(len(arr)):
        need = target - arr[i]
        if need in my_dict:
            return [my_dict[need], i]
        else:
            my_dict[arr[i]] = i


my_arr = [3, 2, 4]
print(two_sum(arr=my_arr, target=6))
