def reverse_words(s: str) -> str:
    # convert to list(for in place)
    new_s = list(s)

    # reverse helper
    def reverse(left, right):
        while left < right:
            new_s[left], new_s[right] = new_s[right], new_s[left]
            left += 1
            right -= 1

    n = len(new_s)
    reverse(0, n - 1)

    start = 0
    for end in range(0, len(new_s) + 1):
        if end == n or new_s[end] == " ":
            reverse(start, end - 1)
            start = end + 1

    print(new_s)
    # words = []
    # word = ""
    # for char in new_s:
    #     if char == " ":
    #         if word != "":
    #             words.append(word)
    #             word = ""
    #     else:
    #         word += char
    # if word != "":
    #     words.append(word)
    #
    # reversed_str = ""
    # for i in range(len(words)):
    #     if i == len(words) - 1:
    #         reversed_str += words[i]
    #     else:
    #         reversed_str += words[i] + " "
    # return reversed_str

    i = 0
    j = 0
    while j < n:
        # skipping space
        while j < n and new_s[j] == " ":
            j += 1
        # swap i and j
        while j < n and new_s[j] != " ":
            new_s[i] = new_s[j]
            i += 1
            j += 1
        while j < n and new_s[j] == " ":
            j += 1
        if j < n:
            new_s[i] = " "
            i += 1
    print(new_s)


my_string = ' hello  world  '
print(reverse_words(s=my_string))
