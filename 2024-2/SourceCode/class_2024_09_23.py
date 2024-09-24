def matmult(A,B):
    n = len(A)
    m = len(B)
    p = len(B[0])
    C = [[0,0],[0,0]]

    for i in range(n):
        for j in range(p):
            for k in range(m):
                C[i][j] = C[i][j] +  A[i][k]*B[k][j]
            
    return C

def exam1_p1(M):
    for i in range(0,len(M)):
        for j in range(0,len(M[0])):
            if (i%2==0 and j%2==1):
                print(M[i][j],end=' ')
        if (i%2 == 0):
            print()


if __name__ == '__main__':
    M = [[1,2,3,4],
         [5,6,7,8],
         [9,10,11,12],
         [13,14,15,16]]
    
    exam1_p1(M)

    A = [[1,2],
         [3,4]]
    B = [[5,6],
         [7,8]]
    
    C = matmult(A,B)

    print(C)