def manip_max(arr,n,t):
    new_arr=[0 for _ in range(n)]
    for thing in arr:
        new_arr[thing[0]-1]+=thing[2]
        if thing[1]<n:
            new_arr[thing[1]]-=thing[2]
    sumi=0
    max_global=0
    for thing in new_arr:
        sumi+=thing
        if sumi>max_global:
            max_global=sumi
    return max_global

if __name__=='__main__':
    n,t=map(int,input().split())
    arr=[]
    for i in range(t):
        arr.append(list(map(int,input().split())))
    print(manip_max(arr,n,t))
