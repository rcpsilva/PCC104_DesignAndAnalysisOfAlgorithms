def algorithm(x):
    result = 0
    for i in x:
        for j in x:
            for k in x:
                for l in x:
                    result += i * j * k * l
    return result
