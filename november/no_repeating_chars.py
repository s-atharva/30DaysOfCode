def find_no_repeating_chars(s):
    i, j = 0, 0
    my_dict = {}
    max_len = 0
    n = len(s)
    while j < n:
        if s[j] in my_dict:
            my_dict[s[j]] += 1
        else:
            my_dict[s[j]] = 1

        if len(my_dict) < j - i + 1:
            while len(my_dict) < j - i + 1:
                my_dict[s[i]] -= 1
                if my_dict[s[i]] == 0:
                    del my_dict[s[i]]
                i += 1
            j += 1

        elif len(my_dict) == j - i + 1:
            max_len = max(max_len, j - i + 1)
            j += 1
    return max_len


s = 'aaaaath'
print(find_no_repeating_chars(s))
