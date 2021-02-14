def bounded_ks(val,wt,w,n):
    val_arr=[[0 for i in range(w+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(w+1):
            if wt[i-1]<=j:
                val_arr[i][j]=max(val_arr[i-1][j-wt[i-1]]+val[i-1],val_arr[i-1][j])
    return val_arr[n][w]

if __name__=='__main__':
    val=[60,100,120]
    wt=[10,20,30]
    w=50
    n=len(wt)
    print(bounded_ks(val,wt,w,n))
