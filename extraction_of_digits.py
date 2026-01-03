n = 5873
num = n
count = 0
while num > 0:
    last_digit = num % 10
    print(last_digit, end=" ")
    count += 1
    num = num // 10

print()
print(f'Count of number is {count}')
