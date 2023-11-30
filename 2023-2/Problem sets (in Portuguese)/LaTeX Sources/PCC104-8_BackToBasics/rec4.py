def algorithm_logn_cost(n):
    if n <= 1:
        return n
    else:
        return algorithm_logn_cost(n // 2) + 1
