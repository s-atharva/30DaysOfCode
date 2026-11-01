my_arr = [2, 3, 5, 2, 9, 7, 1]
k = 3
max_total = 0
for i in range(len(my_arr) - k + 1):
    total = 0
    for j in range(i, i + k):
        total += my_arr[j]
        max_total = max(max_total, total)

print(max_total)
