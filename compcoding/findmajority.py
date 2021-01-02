def findmaj(arr):
    if len(arr)==0:
        return '',0
    if len(arr)==1:
        return arr[0],1
    a1,b1=findmaj(arr[:len(arr)//2])
    a2,b2=findmaj(arr[len(arr)//2:])
    count=0
    if b1>b2:
        for thing in arr[len(arr)//2+1:]:
            if thing==a1: count+=1
        return a1,b1+count
    else:
        for thing in arr[:len(arr)//2]:
            if thing==a2: count+=1
        return a2,b2+count

n=int(input())
arr=list(input().split())
thing,freq=findmaj(arr)
if freq>n/2:
    print(thing)
else:
    print(0)
