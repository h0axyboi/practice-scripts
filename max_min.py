if __name__ == '__main__':
    n=int(input())
    k=int(input())
    arr=[]
    for _ in range(n):
        arr.append(int(input()))
    arr.sort()
    mindiff=arr[k-1]-arr[0]
    for i in range(1,n-k+1):
        if arr[i+k-1]-arr[i]<mindiff:
            mindiff=arr[i+k-1]-arr[i]
    print(mindiff)
