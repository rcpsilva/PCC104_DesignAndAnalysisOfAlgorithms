def r_insertionSort(A,end):
    if end == 1:
        return
    else:
        r_insertionSort(A,end-1)
        v = A[end-1]
        j = end-2
        while j>=0 and v<A[j]:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = v 

def insertionSort(A):

    for i in range(1,len(A)):
        v = A[i]
        j = i-1
        while j >= 0 and v<A[j]:
            A[j+1] = A[j]
            j-=1
        A[j+1] = v

def insertionSort2(A):

    for i in range(1,len(A)):
        v = A[i]
        index = None
        for j in range(i-1,-2,-1):
            index = int(j)
            if v > A[j]:
                break
            A[j+1] = A[j]
        A[index+1] = v


A = [89,45,68,90,29,34,17]

print(A)
insertionSort2(A)
print(A)