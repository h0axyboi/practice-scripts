def getnum(n):
    return n*(n+1)//2

def getcount(n,s):
    arr=[]
    for c in s:
        if arr==[] or arr[-1][0]!=c:
            arr.append([c,1])
            continue
        arr[-1][1]+=1
    count=0
    for thing in arr:
        count+=getnum(thing[1])
    for i in range(1,len(arr)-1):
        if arr[i][1]==1 and arr[i-1][0]==arr[i+1][0]:
            count+=min(arr[i-1][1],arr[i+1][1])
    return count

n=int(input())
s=input()
print(getcount(n,s))
