n = 1234321
num = n
result = 0
while num > 0:
    last_index = num % 10
    result = (result * 10) + last_index
    num = num // 10
print(n == result)
