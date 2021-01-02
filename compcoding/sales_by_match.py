def getpairs(n,arr):
    d={}
    count=0
    for thing in arr:
        if d.get(thing,0)==1:
            count+=1
            d.pop(thing)
        else:
            d[thing]=1
    return count

n=int(input())
arr=list(map(int,input().split()))
print(getpairs(n,arr))
