class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return 'Stack is Empty'
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return 'Stack is Empty'
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


def reverse_string(s):
    my_stack = Stack()

    for elem in s:
        my_stack.push(elem)

    reverse_str = ''

    while not my_stack.is_empty():
        reverse_str += my_stack.pop()

    return reverse_str


print(reverse_string(s='abc'))
