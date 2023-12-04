def recursive_algorithm(n):
    if n == 1:
        return 1
    else:
        val = 0
        for i in range(3):
            val += recursive_algorithm(n - 1)

        return val     