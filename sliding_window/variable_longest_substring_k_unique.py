def find_longest_substring(s, k):
    i = 0
    j = 0
    map = {}
    maxi = 0
    while j < len(s):
        if s[j] in map:
            map[s[j]] += 1
        else:
            map[s[j]] = 1

        if len(map) < k:
            j += 1

        elif len(map) == k:
            maxi = max(maxi, j - i + 1)
            j += 1

        else:
            while len(map) > k:
                map[s[i]] -= 1
                if map[s[i]] == 0:
                    del map[s[i]]
                i += 1
            j += 1
    return maxi


S = "aabacbebebe"
K = 3
print(find_longest_substring(s=S, k=K))
