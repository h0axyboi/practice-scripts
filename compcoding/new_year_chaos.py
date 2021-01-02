def min_bribe(arr,n):
    ans=0
    for i in range(n-1,-1,-1):
        if arr[i]-i-1>2:
            return 'Too chaotic'
        for j in range(max(0,arr[i]-2),i):
            if arr[j]>arr[i]:
                ans+=1
    return ans

for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    print(min_bribe(arr,n))
