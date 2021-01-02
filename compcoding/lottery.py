def lookinarr(arr,num):
    count=0
    i=0
    while i<len(arr) and num>=arr[i][0]:
        if arr[i][0]<=num<=arr[i][1]:
            count+=1
        i+=1
    return count

n,p=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))
queries=list(map(int,input().split()))
answers=[]
arr.sort()
for num in queries:
    answers.append(lookinarr(arr,num))
for num in answers:
    print(num,end=' ')
