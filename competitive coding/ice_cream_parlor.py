def search(arr2,thing,a,b):
    m=(a+b-1)//2
    if a==b:
        return (False,0)
    if arr2[m]==thing:
        return (True,m)
    if arr2[m]>thing:
        return search(arr2,thing,a,m)
    else:
        return search(arr2,thing,m+1,b)


for _ in range(int(input())):
    t=int(input())
    n=int(input())
    arr=list(map(int,input().split()))
    arr2=sorted(arr)
    for i1,thing in enumerate(arr2):
        (x,i2)=search(arr2,t-thing,0,len(arr2))
        if x:
            break
    a=arr.index(arr2[i1])+1
    b=arr.index(arr2[i2])+1
    if(arr.index(arr2[i1])==arr.index(arr2[i2])):
        a=arr.index(arr2[i1])+1
        del arr[arr.index(arr2[i1])]
        b=arr.index(arr2[i2])+2
    print(min(a,b),max(a,b))
