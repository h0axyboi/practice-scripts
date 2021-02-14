def do_the_thing(n,arr):
    num_swaps=0
    for i in range(n-1,0,-1):
        for j in range(0,i):
            if arr[j+1]<arr[j]:
                num_swaps+=1
                temp=arr[j+1]
                arr[j+1]=arr[j]
                arr[j]=temp
    return num_swaps,arr[0],arr[-1]

if __name__ == '__main__':
    n=int(input())
    arr=list(map(int,input().split()))
    num_swaps,fe,le=do_the_thing(n,arr)
    print('Array is sorted in {} swaps.'.format(num_swaps))
    print('First Element: {}'.format(fe))
    print('Last Element: {}'.format(le))
