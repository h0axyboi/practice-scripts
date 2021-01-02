#Program to find the longest subsequence of two sequences
def get_sub(x1,x2):
    answer=[]
    max_val=max(len(x1),len(x2))
    D=[[max_val]*(len(x1)+1) for _ in range(len(x2)+1)]
    for i in range(len(x1)+1):
        D[0][i]=i
    for i in range(len(x2)+1):
        D[i][0]=i
    for i in range(1,len(x2)+1):
        for j in range(1,len(x1)+1):
            diff=0 if x1[j-1]==x2[i-1] else 1
            D[i][j]=min(D[i-1][j]+1,D[i][j-1]+1,D[i-1][j-1]+diff)
    pointer=[len(x2),len(x1)]
    opt=D[len(x2)][len(x1)]
    while pointer[0] and pointer[1]:
        temp=pointer
        i=pointer[0]
        j=pointer[1]
        pointer=min([[i-1,j],[i,j-1],[i-1,j-1]],key=lambda a:D[a[0]][a[1]])
        if D[pointer[0]][pointer[1]]==D[temp[0]][temp[1]]:
            answer.append(x2[temp[0]-1])
    return answer

def get_all_sub(arr):
    common_sub=arr[0]
    for i in range(len(arr)-1):
        common_sub=get_sub(common_sub,arr[i+1])
    print(common_sub)
    return common_sub

arr=[]
for _ in range(int(input())):
    arr.append(list(input().split()))
print(len(get_all_sub(arr)))
