def countjumps(n,arr):
    curr=0
    count=0
    while True:
        if curr+2<n and arr[curr+2]==0:
            count+=1
            curr+=2
            continue
        elif curr+1<n and arr[curr+1]==0:
            count+=1
            curr+=1
            continue
        break
    return count

n=int(input())
arr=list(map(int,input().split()))
print(countjumps(n,arr))
