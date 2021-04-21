def divide_n(n, m):
    if n < 1 or m < 1:
        return 0
    elif n == 1 or m == 1:
        return 1
    elif n < m:
        return divide_n(n, n)
    elif n == m:
        return divide_n(n, m-1) + 1
    else:
        return divide_n(n, m-1) + divide_n(n-m, m)


n = int(input('Input a number: '))
print(f'The divide of {n} has {divide_n(n,n)} methods ')
