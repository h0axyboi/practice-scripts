def do_left_rotate(arr,n,d):
    s=''
    for i in range(d%n,d%n+n):
        s+=arr[i%n]+' '
    return s.rstrip()

n,d=map(int,input().split())
arr=list(input().split())
print(do_left_rotate(arr,n,d))
