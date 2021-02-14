def getminabsdiff(arr,n):
    arr.sort()
    ans=abs(arr[0]-arr[1])
    for i in range(n-1):
        if abs(arr[i]-arr[i+1])<ans:
            ans=abs(arr[i]-arr[i+1])
    return ans

if __name__=='__main__':
    n=int(input())
    arr=list(map(int,input().split()))
    print(getminabsdiff(arr,n))
