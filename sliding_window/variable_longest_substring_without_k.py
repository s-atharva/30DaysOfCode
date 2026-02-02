def find_longest_substring(s):
    i = 0
    j = 0
    maxi = 0
    frequency = {}
    while j < len(s):
        if s[j] in frequency:
            frequency[s[j]] += 1
        else:
            frequency[s[j]] = 1

        if len(frequency) == j - i + 1:
            maxi = max(maxi, j - i + 1)
            j += 1

        else:
            while len(frequency) < j - i + 1:
                frequency[s[i]] -= 1
                if frequency[s[i]] == 0:
                    del frequency[s[i]]
                i += 1
            j += 1

    return maxi


S = 'pwwkew'
print(find_longest_substring(s=S))
