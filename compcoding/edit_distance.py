def ed_dist(a,b):
    D=[[100]*(len(a)+1) for _ in range(len(b)+1)]
    for i in range(len(a)+1):
        D[0][i]=i
    for j in range(len(b)+1):
        D[j][0]=j
    for i in range(1,len(b)+1):
        for j in range(1,len(a)+1):
            to_add=0 if a[j-1]==b[i-1] else 1
            D[i][j]=min(D[i][j-1]+1,D[i-1][j]+1,D[i-1][j-1]+to_add)
    return D[len(b)][len(a)]

w1=input()
w2=input()
print(ed_dist(w1,w2))
