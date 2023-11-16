
def fib(n):

    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fib(n-1) + fib(n-2)

def fib_bu(n):

    m = [-1 for _ in range(n+1)]
    m[0] = 0
    m[1] = 1

    for i in range(2,n+1):
        m[i] = m[i-1]+m[i-2]

    return m[n]

def fib_td(n):
    m = [-1 for _ in range(n+1)]
    return _fib_td(n,m)

def _fib_td(n,m):

    if n == 0:
        m[0] = 0
        return 0
    if n == 1:
        m[1] = 1
        return 1
    
    f1 = _fib_td(n-1,m) if m[n-1]==-1 else m[n-1]
    f2 = _fib_td(n-2,m) if m[n-2]==-1 else m[n-2]

    m[n] = f1+f2

    return f1+f2

if __name__ == '__main__':

    n = 35
    
    print(f'bu {fib_bu(n)}')
    print(f'td {fib_td(n)}')
    print(f'raw {fib(n)}')

    
    