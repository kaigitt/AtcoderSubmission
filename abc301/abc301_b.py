import math

N = int(input())
A = list(map(int, input().split()))
res = []

for i in range(N-1):
    if(A[i]+1 < A[i+1]):
        tmp = A[i+1]-A[i]
        for j in range(tmp):
            res.append(A[i]+j)
    elif(A[i]-1 > A[i+1]):
        tmp = A[i]-A[i+1]
        for j in range(tmp):
            res.append(A[i]-j)
    else:
        res.append(A[i])

res.append(A[N-1])
    
print(*res)