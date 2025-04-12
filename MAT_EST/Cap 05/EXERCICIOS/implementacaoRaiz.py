import math


def somaVetores(A, B):
    C = []
    for i in range(len(A)):
        C.append(A[i] + B[i])
    print(C)
    
#START    
A = [1,2,3]
B = [4,5,6]
somaVetores(A,B)