# cook your dish here
K,G,M = map(int, input().split())

g,m = 0,0

for i in range(K):
    # print("pre", g, m)
    if(g == G):
        g = 0
    elif(m == 0):
        m = M
    else:
        if(g + m > G):
            m = g + m - G
            g = G
            
        else: # g + m <= G
            
            g = g + m
            m = 0
    # print("end", g, m)

print(g, m)