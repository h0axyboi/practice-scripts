def partition(arr,low,high):
    pivot=arr[low]
    j=low
    for i in range(low+1,high+1):
        if arr[i]<=pivot:
            j+=1
            space=arr[j]
            arr[j]=arr[i]
            arr[i]=space
    space=arr[low]
    arr[low]=arr[j]
    arr[j]=space
    return j

def quicksort(arr,low,high):
    if len(arr)<=1 or low>high: return
    m=partition(arr,low,high)
    quicksort(arr,low,m-1)
    quicksort(arr,m+1,high)

arr=list(map(int,input().split()))    
quicksort(arr,0,len(arr)-1)
print(arr)
