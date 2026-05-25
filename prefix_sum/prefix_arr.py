my_arr = [1, 7, 3, 6, 5, 6]
n = len(my_arr)
prefix_sum = [0] * (n + 1)

for i in range(1, len(prefix_sum)):
    prefix_sum[i] = prefix_sum[i - 1] + my_arr[i - 1]

print(prefix_sum)
