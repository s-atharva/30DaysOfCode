def find_kth_grammar(n, k):
    if n == 1:
        return 0

    mid = int((2 ** n) / 2)

    if k <= mid:
        find_kth_grammar(n - 1, k)
    else:
        find_kth_grammar(n - 1, k - mid)


find_kth_grammar(n=4, k=3)
