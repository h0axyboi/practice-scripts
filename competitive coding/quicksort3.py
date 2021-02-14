def partition(arr,l,r):
    pivot=arr[l]
    j=l
    t=r
    i=l+1
    while i<=r:
        if t<i:
            break
        if arr[i]<pivot:
            j+=1
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
        elif arr[i]>pivot:
            arr[t],arr[i]=arr[i],arr[t]
            t-=1
        else:
            i+=1
    arr[l],arr[j]=arr[j],arr[l]
    return j,t


def quicksort3(arr,l,r):
    if l>r:
        return
    m1,m2=partition(arr,l,r)
    quicksort3(arr,l,m1-1)
    quicksort3(arr,m2+1,r)

arr=list(map(int,input().split()))
quicksort3(arr,0,len(arr)-1)
print(arr)
