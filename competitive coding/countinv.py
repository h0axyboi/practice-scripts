def merge(arr,temp,l,mid,r):
    i=l
    j=mid+1
    k=l
    count=0
    while i<=mid and j<=r:
        if arr[i]<=arr[j]:
            temp[k]=arr[i]
            k+=1
            i+=1
        else:
            temp[k]=arr[j]
            count+=mid-i+1
            k+=1
            j+=1
    while i<=mid:
        temp[k]=arr[i]
        i+=1
        k+=1
    while j<=r:
        temp[k]=arr[j]
        j+=1
        k+=1
    for i in range(l,r+1):
        arr[i]=temp[i]
    return count

def _mergesort(arr,temp,l,r):
    count=0
    if l>=r:
        return 0
    mid=(l+r)//2
    count+=_mergesort(arr,temp,l,mid)
    count+=_mergesort(arr,temp,mid+1,r)
    count+=merge(arr,temp,l,mid,r)
    return count

def mergesort(arr,n):
    temp=[0]*n
    return _mergesort(arr,temp,0,n-1)

n=int(input())
arr=list(map(int,input().split()))
print(mergesort(arr,n))
