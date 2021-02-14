if __name__=='__main__':
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    arr.sort(reverse=True)
    ans=0
    for i,thing in enumerate(arr):
        ans+=((i//k)+1)*thing
    print(ans)
