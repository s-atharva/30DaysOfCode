def allocate_min_no_pages_n_2(arr, k):
    pages_list = list()
    for i in range(1, len(arr)):
        s1 = sum(my_arr[:i])
        s2 = sum(my_arr[i:])
        pages_list.append((s1, s2))
    print(max(max(pages_list)))


my_arr = [10, 20, 30, 40]
k = 2
allocate_min_no_pages_n_2(arr=my_arr, k=k)
