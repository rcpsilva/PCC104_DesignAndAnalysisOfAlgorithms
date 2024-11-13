def recursive_insertion_sort(A,end):

    if end == 1:
        return 
    else:
        recursive_insertion_sort(A,end-1)
        j = end-2
        v = A[end-1]
        while j>=0 and v<A[j]:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = v



def insertion_sort(A):

    end = 1
    v = A[end-1]

    for i in range(1,len(A)):
        j = i-1
        v = A[i]
        while j>=0 and v <= A[j]:
            A[j+1] = A[j]
            j-=1
        A[j+1] = v


A = [89,45,68,90,29,34,17]
B = [89,45,68,90,29,34,17]


print(A)
recursive_insertion_sort(A,len(A))
print(A)


print(B)
insertion_sort(B)
print(B)




