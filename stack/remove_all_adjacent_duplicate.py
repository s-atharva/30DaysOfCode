def remove_all_duplicate(s):
    stack = []
    for char in s:
        if len(stack) > 0 and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)


my_str = ['a', 'b', 'b', 'a', 'c', 'a']
print(remove_all_duplicate(s=my_str))
