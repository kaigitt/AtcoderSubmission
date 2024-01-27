import math

N = int(input())

S = str(bin(N))

cnt = 0
for i in range(len(S)):
    if(S[i] == "0"):
        cnt += 1
    else:
        cnt = 0
    
print(cnt)