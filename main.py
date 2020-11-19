import numpy as np
import numpy.linalg

#fonction qui vérifie est ce que la matrice triangulaire supérieure
def trisup(A):
    n=len(A)
    for i in range (1,n):
        for j in range (i):
            if A[i][j] != 0:
                return False
    return True
############################################################################################################################################################################################

#fonction qui vérifie est ce que la matrice triangulaire inférieure
def triinf(A):
    n=len(A)
    for i in range (1,n):
        for j in range (i+1,n):
            if A[i][j]!=0:
                return False
    return True

######################################################################################################################################################################

#fonction qui vérifie est ce que les coefficient digonaux est non nuls
def diag_non_nuls(A):
    n=len(A)
    for i in range (n):
            if A[i][i]==0:
                return False
    return True

######################################################################################################################################################################################


def meth_remontee(A,B):
    if trisup(A) and diag_non_nuls(A):
        A=np.array(A)
        n=len(A)
        x=[0]*n
        x[n-1]=B[n-1]/A[n-1][n-1]
        for i in range (n-2,0):
            s=0
            for j in range (i+1,n-1):
                s=s+A[i][j]*x[j]
            x[i]=(B[i]-s)/A[i][i]
    return x


#############################################################################################

def meth_desc(A,B):
    if triinf(A) and diag_non_nuls(A):
        A=np.array(A)
        n=len(A)
        x=[0]*n
        x[0]=float(B[0]/A[0][0])
        for i in range (1,n):
            s=0
            for j in range (0,i-1):
                s=s+float(A[i][j]*x[j])
            x[i]=float((B[i]-s)/A[i][i])
    return x

def meth_remontee(A,B):
    A=np.array(A)
    n=len(A)
    x = []
    for i in range(n):
            x.append(0)
    if trisup(A) and diag_non_nuls(A):
        x[n-1]=B[n-1]/A[n-1] [n-1]
        for i in range (n-2,0):
            s=0
            for j in range (i+1,n-1):
                s += (A[i][j]*x[j])
            x[i]=(B[i]-s)/A[i][i]
    return x



a = [[8,9,7],[0,5,1],[0,0,2]]
b = [5,2,6]

print(meth_remontee(a,b))


















