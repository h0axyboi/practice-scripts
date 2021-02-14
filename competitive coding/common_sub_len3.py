def get_sub_len(a1,a2,a3):
    D=[[[0]*(len(a1)+1) for _ in range(len(a2)+1)] for __ in range(len(a3)+1)]
    for i in range(len(a3)+1):
        for j in range(len(a2)+1):
            for k in range(len(a1)+1):
                if i==0 or j==0 or k==0:
                    D[i][j][k]=0
                elif a3[i-1]==a2[j-1]==a1[k-1]:
                    D[i][j][k]=D[i-1][j-1][k-1]+1
                else:
                    D[i][j][k]=max(D[i-1][j][k],D[i][j-1][k],D[i][j][k-1])
    return D[len(a3)][len(a2)][len(a1)]

n1=int(input())
a1=list(input().split())
n2=int(input())
a2=list(input().split())
n3=int(input())
a3=list(input().split())
print(get_sub_len(a1,a2,a3))
