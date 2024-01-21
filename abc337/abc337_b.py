import math


#N, S = map(int, input().split())

#N = int(input())
#A = list(map(int, input().split()))
#P = list(map(int, input().split()))
S = input()

for a in range(0, 101):
    for b in range(0, 101):
        for c in range(0, 101):
            if S == 'A' * a + 'B' * b + 'C' * c:
                print("Yes")
                exit()

print("No")