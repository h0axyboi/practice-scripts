def getlowercount(val,arr,l,r):
    if (r<=0 or l>=r):
        return 0
    m=(l+r)//2
    if(arr[m]<=val):
        if(m+1>len(arr)-1):
            return len(arr)
        if(arr[m+1]>val):
            return m+1
        else:
            return getlowercount(val,arr,m+1,r)
    else:
#        print(l,m)
        return getlowercount(val,arr,l,m)

def get_triple_sum(a,b,c):
    a1,b1,c1,ans=0,0,0,0
    xa,xb,xc=len(a),len(b),len(c)
    while b1<xb:
        a1=getlowercount(b[b1],a,0,xa)
        c1=getlowercount(b[b1],c,0,xc)
#        print(a1,c1,b[b1],c,xc)
        ans+=a1*c1
        b1+=1
    return ans

n1,n2,n3=tuple(map(int,input().split()))
a=sorted(set(list(map(int,input().split()))))
b=sorted(set(list(map(int,input().split()))))
c=sorted(set(list(map(int,input().split()))))
#print(a,b,c)
print(get_triple_sum(a,b,c))
