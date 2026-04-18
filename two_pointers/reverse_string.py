def reverse_str(s: str) -> str:
    reversed_str = list(s)
    i = 0
    j = len(s) - 1
    while i < j:
        reversed_str[i], reversed_str[j] = reversed_str[j], reversed_str[i]
        i += 1
        j -= 1
    return reversed_str


my_string = 'Atharva'
print(my_string[2])
print(reverse_str(s=my_string))
