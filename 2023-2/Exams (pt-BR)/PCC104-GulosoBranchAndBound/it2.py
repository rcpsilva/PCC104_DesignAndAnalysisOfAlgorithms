def algorithm(x):
    result = 0
    for i in range(len(x)-1):
        for j in range(len(x)-2):
            for k in range(len(x)-3):
                result += i * j * k
    return result
