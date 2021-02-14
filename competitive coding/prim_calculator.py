def min_calc(n):
    arr=[0]
    for i in range(1,n+1):
        mintoadd=arr[i-1]+1
        if i%3==0:
            mintoadd=min(mintoadd,arr[i//3])
        if i%2==0:
            mintoadd=min(mintoadd,arr[1%2])
        arr.append(mintoadd)
    answer=[n]
    while n>1:
        arr1,arr2=[],[]
        if n%3==0:
            arr1.append(n//3)
            arr2.append(arr[n//3])
        if n%2==0:
            arr1.append(n//2)
            arr2.append(arr[n//2])
        arr1.append(n-1)
        arr2.append(arr[n-1])
        n=arr1[arr2.index(min(arr2))]
        answer.append(n)
    answer.reverse()
    return answer,len(answer)-1



n=int(input())
arr,a=min_calc(n)
print(a)
for thing in arr:
    print(str(thing) , end=' ')
