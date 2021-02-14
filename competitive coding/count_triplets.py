def get_count(arr,n,r):
    gp={}
    for thing in arr:
        gp[thing]=gp.get(thing,0)+1
    count=0
    left={}
    for thing in arr:
        gp[thing]-=1
        if thing%r==0:
            if thing//r in left and thing*r in gp:
                count+=left[thing//r]*gp[thing*r]
        left[thing]=left.get(thing,0)+1
    return count

if __name__ == '__main__':
    n,r=map(int,input().split())
    arr=list(map(int,input().split()))
    print(get_count(arr,n,r))
