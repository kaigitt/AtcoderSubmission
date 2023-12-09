import math


N = int(input())
S = input()


tmp = ""
for i in range(N):
    if(S[i] == "|" or S[i] == "*"):
        tmp += S[i]

if("|*|" in tmp):
    print("in")
else:
    print("out")