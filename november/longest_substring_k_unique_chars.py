def long_substring_k_unique_chars(my_str, k):
    i = 0
    j = 0
    n = len(my_str)
    max_len = 0
    my_dict = {}
    while j < n:
        if my_str[j] in my_dict:
            my_dict[my_str[j]] += 1
        else:
            my_dict[my_str[j]] = 1

        if len(my_dict) < k:
            j += 1

        elif len(my_dict) == k:
            max_len = max(max_len, j - i + 1)
            j += 1

        elif len(my_dict) > k:
            while len(my_dict) > k:
                my_dict[my_str[i]] -= 1
                if my_dict[my_str[i]] == 0:
                    del my_dict[my_str[i]]
                i += 1
            j += 1
    return max_len


my_str = 'aabacbebebe'
k = 3
print(long_substring_k_unique_chars(my_str, k))
