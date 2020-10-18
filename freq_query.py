from collections import defaultdict

def freq_query(arr):
    d=defaultdict(int)
    f=defaultdict(int)
    ans=[]
    for action,x in arr:
        if action==1:
            if f[d[x]]:
                f[d[x]]-=1
            d[x]+=1
            f[d[x]]+=1
        elif action==2:
            if d[x]:
                f[d[x]]-=1
                d[x]-=1
                f[d[x]]+=1
        elif action==3:
            ans.append(1 if f[d[x]] else 0)
    return ans

if __name__ == '__main__':
    t=int(input())
    arr=[]
    for i in range(t):
        arr.append(map(int,input().split()))
    x=freq_query(arr)
    for thing in x:
        print(thing)
