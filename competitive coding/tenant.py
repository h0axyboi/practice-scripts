def getvisits(n,ri,li):
    res=0
    coords=''
    while n>0:
        minr=min(ri)
        licop=li.copy()
        for point in licop:
            if point<=minr:
                deli=li.index(point)
                del li[deli]
                del ri[deli]
        res+=1
        coords+=str(minr)+' '
        n=len(ri)
    return res,coords.rstrip()

print('Given a set of timings, the goal is to find the minimum number of visits to see all the tenants who are only present in the given intervals')
n=int(input('Enter the number of tenants: '))
print('In each line, enter the entry time and leaving time of each tenant as space separated integers')
ri,li=[],[]
for _ in range(n):
    inp=list(map(int,input().split()))
    li.append(inp[0])
    ri.append(inp[1])
res,coords=getvisits(n,ri,li)
print(res)
print(coords)
