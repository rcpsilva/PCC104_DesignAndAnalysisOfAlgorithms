def recursive_algorithm(n):
    if n == 1:
        return 0
    else:
        return recursive_algorithm(n - 1) + 5