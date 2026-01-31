def count_anagram_str(my_string: str, pattern: str) -> int:
    dict_count = {}
    k = len(pattern)
    n = len(my_string)
    for letter in pattern:
        if letter in dict_count:
            dict_count[letter] += 1
        else:
            dict_count[letter] = 1

    anagram_count = 0

    for i in range(0, n - k + 1):
        dict_2 = {}
        for j in range(i, i + k):
            ch = my_string[j]
            if ch in dict_2:
                dict_2[ch] += 1
            else:
                dict_2[ch] = 1
        if dict_count == dict_2:
            anagram_count += 1
    return anagram_count


def count_anagram_str_sliding_window(my_string, pattern):
    k = len(pattern)

    str_dict = {}
    for letter in pattern:
        if letter in str_dict:
            str_dict[letter] += 1
        else:
            str_dict[letter] = 1

    count = 0
    i, j = 0, 0
    temp_dict = {}

    while j < len(my_string):
        if my_string[j] in temp_dict:
            temp_dict[my_string[j]] += 1
        else:
            temp_dict[my_string[j]] = 1

        if j - i + 1 < k:
            j += 1

        elif j - i + 1 == k:
            if str_dict == temp_dict:
                count += 1

            temp_dict[my_string[i]] -= 1
            if temp_dict[my_string[i]] == 0:
                del temp_dict[my_string[i]]

            i += 1
            j += 1
    return count


s = 'aabaabaa'
p = 'aaba'
# print(count_anagram_str(my_string=s, pattern=p))
print(count_anagram_str_sliding_window(my_string=s, pattern=p))
