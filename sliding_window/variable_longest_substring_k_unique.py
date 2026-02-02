def find_longest_substring(s, k):
    i = 0
    j = 0
    frequency = {}
    maxi = float('-inf')

    while j < len(s):
        if s[j] in frequency:
            frequency[s[j]] += 1
        else:
            frequency[s[j]] = 1

        if len(frequency) < k:
            j += 1

        elif len(frequency) == k:
            maxi = max(maxi, j - i + 1)
            j += 1

        else:
            while len(frequency) > k:
                frequency[s[i]] -= 1
                if frequency[s[i]] == 0:
                    del frequency[s[i]]
                i += 1
            j += 1
    return maxi


S = "aabacbebebe"
K = 3
print(find_longest_substring(s=S, k=K))
