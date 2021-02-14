def unbounded_ks(w,n,val,wt):
    val_arr=[0 for i in range(w+1)]
    for i in range(w+1):
        for j in range(n):
            if wt[j]<=i:
                val_arr[i]=max(val_arr[i],val_arr[i-wt[j]]+val[j])
    return val_arr[w]

if __name__=='__main__':
    w = 10
    val = [30,14,16,9]
    wt = [6,3,4,2]
    n = len(val)
    print(unbounded_ks(w, n, val, wt))
