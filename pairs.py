def search(a,val,l,r):
    if l==r:
        return False
    m=(l+r-1)//2
    if a[m]==val:
        return True
    if a[m]>val:
        return search(a,val,l,m)
    else:
        return search(a,val,m+1,n)

(n,d)=tuple(map(int,input().split()))
a=list(map(int,input().split()))
a.sort()
ans=0
for i in range(n-1):
    if (search(a,a[i]+d,i+1,n)):
        ans+=1
print(ans)
