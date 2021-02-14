n=int(input())
arr=list(map(int,input().split()))
max_arr=[0 for _ in range(n)]
for i in range(n):
    if i==0:
        max_arr[i]=arr[0]
        continue
    if i==1:
        max_arr[i]=max(arr[0],arr[1])
        continue
    a=arr[i]
    b=max_arr[i-1]
    c=max_arr[i-2]+arr[i]
    max_arr[i]=max(a,b,c)
print(max_arr[-1])
