def get_max(w,n,arr):
    maxes=[[0 for i in range(w+1)] for j in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,w+1):
            maxes[i][j]=maxes[i-1][j]
            if arr[i-1]<=j:
                maxes[i][j]=max(maxes[i-1][j],maxes[i-1][j-arr[i-1]]+arr[i-1])
    selected=[]
    a,b=n,w
    while True:
        if n==0:
            break
        if maxes[n-1][w]==maxes[n][w]:
            selected.append(0)
        else:
            selected.append(1)
            w-=arr[n-1]
        n-=1
    selected.reverse()
    return maxes[a][b],selected

def can_you_divide(n,arr):
    if sum(arr)%3!=0:
        return 0
    minisum=sum(arr)//3
    for i in range(3):
        x,y=get_max(minisum,n,arr)
        if x!=minisum:
            return 0
        for i in range(len(y)):
            if y[i]==1:
                arr[i]=0
    return 1

if __name__=='__main__':
    n=int(input())
    arr=list(map(int,input().split()))
    print(can_you_divide(n,arr))
