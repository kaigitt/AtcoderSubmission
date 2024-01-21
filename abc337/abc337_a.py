import math


#N, S = map(int, input().split())

#N = int(input())
#A = list(map(int, input().split()))
#P = list(map(int, input().split()))
N = int(input())

A = 0
B = 0

for i in range(N):
    X,Y = map(int, input().split())
    A += X
    B += Y

if (A > B):
    print("Takahashi")
elif (A < B):
    print("Aoki")
else:
    print("Draw")
