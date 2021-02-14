t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort(reverse=True)
    suma,sumb=0,0
    for i in range(n):
        if i==0:
            suma+=arr[i]
        elif i==1 or i==2:
            sumb+=arr[i]
        elif i%2!=0:
            suma+=arr[i]
        else:
            sumb+=arr[i]
    if suma>sumb:
        print('first')
    elif suma<sumb:
        print('second')
    else:
        print('draw')
