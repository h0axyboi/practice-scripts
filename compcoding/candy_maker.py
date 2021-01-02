import math

def minimumpasseses(m,w,p,n):
    passes=0
    result=math.ceil(n/(m*w))
    resource=0
    while(passes<result):
        stpasses=math.ceil((p-resource)/(m*w))
        resource+=m*w*stpasses
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
        tempresult=passes+stpasses+math.ceil((n-resource)/(m*w))
        result=min(result,tempresult)
        passes+=stpasses
    return result

m,w,p,n=map(int,input().split())
print(minimumpasseses(m,w,p,n))
