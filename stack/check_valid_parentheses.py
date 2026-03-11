def is_valid(s):
    my_stack = []
    for bracket in s:
        if bracket == '(' or bracket == '[' or bracket == '{':
            my_stack.append(bracket)
        else:
            if len(my_stack) == 0:
                return False
            ch = my_stack.pop()
            if bracket == ')' and ch == '(' or bracket == ']' and ch == '[' or bracket == '}' and ch == '{':
                continue
            else:
                return False
    return len(my_stack) == 0


s = '[[]]{}'
print(is_valid(s))
