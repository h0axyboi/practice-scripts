def get_max(w,n,arr):
    maxes=[[0 for i in range(w+1)] for j in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,w+1):
            maxes[i][j]=maxes[i-1][j]
            if arr[i-1]<=j:
                maxes[i][j]=max(maxes[i-1][j],maxes[i-1][j-arr[i-1]]+arr[i-1])
    return maxes[n][w]


if __name__=='__main__':
    w,n=map(int, input().split())
    arr=list(map(int,input().split()))
    print(get_max(w,n,arr))
