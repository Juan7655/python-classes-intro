def of(n, acc1=0, acc2=1):
    if n < 0:
        raise ValueError
    if n == 0:
        return 0
    elif n <= 1:
        return acc2
    else:
        return of(n - 1, acc2, acc1 + acc2)
