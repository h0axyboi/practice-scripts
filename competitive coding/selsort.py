arr=list(map(int,input().split()))
print(arr)
for i in range(len(arr)):
    mini=i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[mini]:
            mini=j
    if i!=mini:
        arr[i]=arr[i]+arr[mini]
        arr[mini]=arr[i]-arr[mini]
        arr[i]=arr[i]-arr[mini]
print(arr)
