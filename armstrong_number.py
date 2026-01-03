def count_of_number(num):
    count = 0
    while num > 0:
        count += 1
        num = num // 10
    return count


def find_armstrong_number(n):
    num = n
    armstrong_number = 0
    count = count_of_number(n)
    while num > 0:
        last_index = num % 10
        armstrong_number += last_index ** count
        num = num // 10

    return armstrong_number


number = 153
print(number == find_armstrong_number(number))
