def one_to_n(n):
    for i in range(n):
        print(i+1)

def one_to_n_rec(n):
    if n==1:
        print(1)
    else:
        # recursão
        one_to_n_rec(n-1)
        print(n)

def n_to_one(n):
    if n==1:
        print(1)
    else:
        print(n)
        n_to_one(n-1)

def fib(n,nm2=0,nm1=1):
    if n>0:
        print(nm2,end=' ')
        fib(n-1,nm1,nm2+nm1)

if __name__ == '__main__':
    n = 4
    fib(n)

