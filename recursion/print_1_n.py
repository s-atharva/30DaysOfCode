def print_1_n(n):
    if n == 0:
        return None
    print_1_n(n - 1)
    print(n)


def print_n_1(n):
    if n == 0:
        return None
    print(n)
    print_n_1(n - 1)


num = 5
# print_1_n(n=num)
print_n_1(5)
