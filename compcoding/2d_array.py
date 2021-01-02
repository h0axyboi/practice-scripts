def getmax_hourglass(arr):
    i,j=0,0
    count=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
    for i in range(4):
        for j in range(4):
            count=max(count,arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
    return count

arr=[]
for _ in range(6):
    arr.append(list(map(int,input().split())))
print(getmax_hourglass(arr))
