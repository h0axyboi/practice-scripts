import math

def minPasses(m,w,p,n):
    resource,passes=0,0
    result=math.ceil(n/(m*w))
    while(passes<result):
        stpasses=math.ceil((p-resource)/(m*w))
        resource+=m*w*stpasses
        passes+=stpasses
        allottable=resource//p
        resource%=p
        if allottable<=(abs(m-w)):
            if m<w:
                m+=allottable
            else:
                w+=allottable
        else:
            allottable-=abs(m-w)
            m=max(m,w)
            w=max(m,w)
            diff=allottable//2
            m+=diff
            w+=allottable-diff
        tempresult=passes+math.ceil((n-resource)/(m*w))
        result=min(result,tempresult)
    return result

m,w,p,n=map(int,input().split())
print(minPasses(m,w,p,n))
