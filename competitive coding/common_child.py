def get_common(a,b):
    arr=[[0 for i in range(len(a)+1)] for j in range(len(b)+1)]
    for i in range(1,len(b)+1):
        for j in range(1,len(a)+1):
            if a[i-1]==b[j-1]:
                arr[i][j]=arr[i-1][j-1]+1
            else:
                arr[i][j]=max(arr[i-1][j],arr[i][j-1])
    return arr[-1][-1]

s1=input()
s2=input()
print(get_common(s1,s2))
