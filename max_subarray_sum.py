from bisect import insort,bisect_right
def maxSubarray(arr, n, m):
    prefix=[0]*n
    curr=0
    for i in range(n):
        curr=(arr[i]%m+curr)%m
        prefix[i]=curr
    pq=[prefix[0]]
    max_sum=max(prefix)
    for i in range(1,n):
        left=bisect_right(pq,prefix[i])
        if left!=len(pq):
            modsum=(prefix[i]-pq[left]+m)%m
            max_sum=max(modsum,max_sum)
        insort(pq,prefix[i])
    return max_sum


for _ in range(int(input())):
    n,m=tuple(map(int,input().split()))
    a=list(map(int,input().split()))
    print(maxSubarray(a,n,m))
