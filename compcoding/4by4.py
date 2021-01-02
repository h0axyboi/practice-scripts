count=0
n=4
for i in range(2**(n*n)):
    bin_num=bin(i)[2:]
    len_bin=len(bin_num)
    str_bin='0'*(n*n-len_bin)+bin_num
    a=[int(c) for c in str_bin]
    ok=0
    for j in range(n):
        if sum(a[n*j:n*(j+1)])%2==0:
            ok=1
        sum_j=0
        for l in range(n):
            sum_j+=a[j+n*l]
        if sum_j%2==0:
            ok=1
    if ok==0:
        count+=1
print(count)
#random comment
