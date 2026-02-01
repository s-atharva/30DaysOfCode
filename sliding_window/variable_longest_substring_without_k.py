def find_longest_substring(s):
    i = 0
    j = 0
    maxi = 0
    my_dict = {}
    while j < len(s):
        if s[j] in my_dict:
            my_dict[s[j]] += 1
        else:
            my_dict[s[j]] = 1

        if len(my_dict) == j - i + 1:
            maxi = max(maxi, j - i + 1)
            j += 1

        else:
            while j - i + 1 > len(my_dict):
                my_dict[s[i]] -= 1
                if my_dict[s[i]] == 0:
                    del my_dict[s[i]]
                i += 1
            j += 1

    return maxi


S = 'pwwkew'
print(find_longest_substring(s=S))
