def len_com_sub(a1,a2):
    D=[[0]*(len(a1)+1) for _ in range(len(a2)+1)]
    for i in range(len(a2)+1):
        for j in range(len(a1)+1):
            if (i==0 or j==0):
                D[i][j]==0
            elif a1[j-1]==a2[i-1]:
                D[i][j]=D[i-1][j-1]+1
            else:
                D[i][j]=max(D[i-1][j],D[i][j-1])
    return D[len(a2)][len(a1)]

n1=int(input())
a1=list(input().split())
n2=int(input())
a2=list(input().split())
print(len_com_sub(a1,a2))
