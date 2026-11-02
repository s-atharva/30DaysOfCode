def count_anagrams(my_string, pattern):
    count = 0
    k = len(pattern)
    for i in range(len(my_string) - k + 1):
        if sorted(my_string[i:i + k]) == sorted(pattern):
            print(my_string[i:i + k])
            count += 1
    return count


def count_anagrams_sw(strr, p):
    n = len(strr)
    i, j = 0, 0

    d = {}
    ans = 0
    k = len(p)

    for ch in p:
        d[ch] = d.get(ch, 0) + 1

    count = len(d)

    while j < n:
        if strr[j] in d:
            d[strr[j]] -= 1

            if d[strr[j]] == 0:
                count -= 1

        if j - i + 1 < k:
            j += 1

        elif j - i + 1 == k:
            if count == 0:
                ans += 1

            if strr[i] in d:
                if d[strr[i]] == 0:
                    count += 1

                d[strr[i]] += 1
            i += 1
            j += 1
    return ans


my_str = 'forxxorfxdofr'
pattern = 'for'
# print(count_anagrams(my_str, pattern))
print(count_anagrams_sw(my_str, pattern))
