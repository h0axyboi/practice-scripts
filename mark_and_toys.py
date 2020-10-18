def num_toys(n,w,arr):
    arr.sort(reverse=True)
    count=0
    while w>0:
        if arr[-1]<=w:
            w-=arr[-1]
            count+=1
            arr.pop()
        else:
            break

    return count

if __name__ == '__main__':
    n,w=map(int,input().split())
    arr=list(map(int,input().split()))
    print(num_toys(n,w,arr))
