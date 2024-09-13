def second_largest(a):

    largest = a[0]

    for i in range(1,len(a)):
        if a[i] > largest:
            largest = a[i]

    sl = a[0] 

    for i in range(1,len(a)):
        if a[i] > sl and a[i] < largest:
            sl = a[i]

    if sl == largest:
        return False

    return sl

def second_largest_v2(a):

    l = a[0]
    sl = -1

    for i in range(1,len(a)):
        if a[i] > l:
            sl = l
            l = a[1]
        elif a[i] > sl:
            sl = a[i]

    if sl == l:
        return -1
    
    return sl

if __name__ == '__main__':

    print(second_largest([12,35,1,10,34,1]))
    print(second_largest([10,10]))

    print(second_largest_v2([12,35,1,10,34,1]))
    print(second_largest_v2([10,10]))
