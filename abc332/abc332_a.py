# cook your dish here
N,S,K = map(int, input().split())

total = 0

for i in range(N):
    P,Q = map(int, input().split())
    total += P * Q

if(total >= S):
    pass
else:
    total = total + K

print(total)