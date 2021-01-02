def merge(p,q):
    r=[]
    while len(p)>0 and len(q)>0:
        if p[0]<q[0]:
            r.append(p[0])
            del p[0]
        else:
            r.append(q[0])
            del q[0]
    r.extend(p)
    r.extend(q)
    return r

def mergesort(arr):
    if len(arr)<=1:
        return arr
    a=arr[:len(arr)//2]
    b=arr[len(arr)//2:]
    return merge(mergesort(a),mergesort(b))

arr=list(map(int,input().split()))
print(mergesort(arr))
