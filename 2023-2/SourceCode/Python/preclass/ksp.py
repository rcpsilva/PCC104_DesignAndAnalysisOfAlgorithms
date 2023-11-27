import numpy as np

def ksp_BU(F,v,w):

    for i in range(F.shape[0]):
        F[i,0] = 0

    for j in range(F.shape[1]):
        F[0,j] = 0

    for i in range(1,F.shape[0]):
        for j in range(1,F.shape[1]):
            F[i,j] = F[i-1,j] if j < w[i-1] else max(F[i-1,j], v[i-1] + F[i-1,j-w[i-1]])
            

def ksp_TD(F,v,w,i,j):

    if j == 0:
        F[i,j] = 0
    
    if i == 0:
        F[i,j] = 0

    if F[i,j] < 0:
        if j < w[i-1]:
            value = ksp_TD(F,v,w,i-1,j)
        else:
            value = max(ksp_TD(F,v,w,i-1,j), v[i-1] + ksp_TD(F,v,w,i-1,j-w[i-1]))

        F[i,j] = value

    return F[i,j]


if __name__ == '__main__':

    #w = [2,1,3,2]
    #v = [12,10,20,15]
    #capacity = 5

    w = [3,2,1,4,5]
    v = [25,20,15,40,50]
    capacity = 6

    F = np.ones((len(w)+1,capacity+1))*-1

    ksp_BU(F,v,w)

    print(F)

    #---------------------------------------------------

    F = np.ones((len(w)+1,capacity+1))*-1

    ksp_TD(F,v,w,len(w),capacity)

    print(F)


