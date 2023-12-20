def print_pares(n):

    if n == 1:
        return

    if n % 2 == 0:
        print(n)

    print_pares(n-1)