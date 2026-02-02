def find_max_toys(s: str, k: int) -> int:
    i = 0
    j = 0
    maxi = 0
    frequency = {}
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


S = 'abaccab'
K = 2
print(find_max_toys(s=S, k=K))
