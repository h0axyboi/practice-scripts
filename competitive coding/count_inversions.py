def merge(a,b):
    r=[]
    count=a[0]+b[0]
    while len(a[1])>0 and len(b[1])>0:
        if a[1][0]<=b[1][0]:
            r.append(a[1][0])
            del a[1][0]
        else:
            r.append(b[1][0])
            del b[1][0]
            count+=len(a[1])
    r.extend(a[1])
    r.extend(b[1])
    return count,r

def get_count(arr,x):
    if x<=1:
        return [0,arr]
    a=arr[:x//2]
    b=arr[x//2:]
    return merge(get_count(a,x//2),get_count(b,(x-x//2)))

n=int(input())
for _ in range(n):
    x=int(input())
    arr=list(map(int,input().split()))
    print(get_count(arr,x)[0])
