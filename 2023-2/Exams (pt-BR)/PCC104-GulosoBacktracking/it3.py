def algorithm(x):
    result = 0
    for i in range(len(x)):
        for j in range(2,len(x)):
            result += i + j
    return result
