def binsearch(arr,num,low,high):
    if len(arr)==0 or low>=high:
        return -1
    mid=(low+high)//2
    if arr[mid]==num:
        return mid
    elif arr[mid]>num:
        high=mid-1
        return binsearch(arr,num,low,high)
    else:
        low=mid+1
        return binsearch(arr,num,low,high)
    return -1

line1=list(map(int,input().split()))
line2=list(map(int,input().split()))
n1,n2=line1[0],line2[0]
arr=line1[1:]
queries=line2[1:]
indices=[]
print(queries)
for num in queries:
    indices.append(binsearch(arr,num,0,len(arr)-1))
for num in indices:
    print(num,end=' ')
