def find_stock_span(arr):
    n = len(arr)
    result = [1] * n
    for i in range(n):
        span = 1
        for j in range(i - 1, -1, -1):
            if arr[j] <= arr[i]:
                span += 1
            else:
                break
        result[i] = span
    return result


def stock_span_n(arr):
    ngl = []
    my_stack = []
    stock_span = []

    for i in range(len(arr)):
        if len(my_stack) == 0:
            ngl.append(-1)

        elif len(my_stack) > 0 and my_stack[-1][0] > arr[i]:
            ngl.append(my_stack[-1][1])

        elif len(my_stack) > 0 and my_stack[-1][0] <= arr[i]:
            while len(my_stack) > 0 and my_stack[-1][0] <= arr[i]:
                my_stack.pop()
            if len(my_stack) == 0:
                ngl.append(-1)
            else:
                ngl.append(my_stack[-1][1])

        my_stack.append([arr[i], i])

    for i in range(len(ngl)):
        stock_span.append(i - ngl[i])

    return stock_span


my_stock = [100, 80, 60, 70, 60, 75, 85]
# print(find_stock_span(arr=my_stock))
print(stock_span_n(arr=my_stock))
