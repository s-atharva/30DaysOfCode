def find_factors_brute(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    print(factors)


def find_factors_better(num):
    factors = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            factors.append(i)
    factors.append(num)
    print(factors)


def find_factors_best(num):
    factors = []
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            factors.append(i)
            temp = num // i
            if temp not in factors:
                factors.append(temp)
    print(sorted(factors))


find_factors_brute(36)
find_factors_better(36)
find_factors_best(36)
