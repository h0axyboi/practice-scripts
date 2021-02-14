t=int(input())
for _ in range(t):
    a=input()
    b=input()
    arr=[[0 for i in range(len(a)+1)] for j in range(len(b)+1)]
    arr[0][0]=1
    for i in range(len(a)):
        if a[i].isupper():
            break
        arr[0][i+1]=1
    for i in range(1,len(b)+1):
        for j in range(1,len(a)+1):
            if a[j-1].isupper():
                if a[j-1]==b[i-1]:
                    arr[i][j]=arr[i-1][j-1]
            else:
                if a[j-1].upper()==b[i-1]:
                    arr[i][j]=arr[i][j-1] or arr[i-1][j-1]
                else:
                    arr[i][j]=arr[i][j-1]
    if arr[-1][-1]:
        print('YES')
    else:
        print('NO')
