def get_min(arr,n):
    count=0
    i=0
    while i<n:
        if arr[i]!=i+1:
            temp=arr[i]
            arr[i]=arr[arr[i]-1]
            arr[temp-1]=temp
            count+=1
            continue
        i+=1
    return count


if __name__=='__main__':
    n=int(input())
    arr=list(map(int,input().split()))
    print(get_min(arr,n))
