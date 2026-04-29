def reverse_word_str(s):
    words = []
    word = ""
    for char in s:
        if char == " ":
            if word != "":
                words.append(word)
                word = ""
        else:
            word += char
    if word != "":
        words.append(word)

    for i in range(len(words) - 1, -1, -1):
        if i == 0:
            print(words[i], end="")
        else:
            print(words[i], end=" ")


my_string = ' the  sky is blue'
new_str = list(my_string)
# reverse_word_str(s=my_string)
# print(reverse(new_str))
# print(new_str)
