def algorithm(n):
    if n <= 1:
        return n
    else:
        a = 0
        for i in range(n):
            a += i

        return a + algorithm(n // 2)
