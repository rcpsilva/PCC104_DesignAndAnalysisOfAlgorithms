def imprimir(A):

    if len(A) == 1:
        print(A[0])
    else:
        print(A[0])
        imprimir(A[1:])

def fib(n):
    if n == 0:
        return 0
    elif n  == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)



imprimir([1,2,3,4])

print(fib(7))
print(fib(10))
print(fib(19))

