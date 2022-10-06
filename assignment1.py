N=int(input(''))
A=[None]*N
for i in range(0,N):
    A[i]=int(input(' '))
M=int(input(''))
B=[None]*M
C=[None]*M
for i in range(0,M):
    B[i]=int(input(' '))


for i in range(0,M):
    for j in range(0,N):
        if(A[j]==B[i]):
            C[i]=1
    if(C[i]!=1):
        C[i]=0
            
for i in range(0,M):
    print(C[i])
