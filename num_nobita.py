def isnobita(n):
    arr=[int(x) for x in str(n)]
    for i in range(len(arr)-1):
        if abs(arr[i+1]-arr[i])!=1:
            return False
    return True

nobita=[]
count=0
for i in range(100):
    if isnobita(i):
        nobita.append(i)
        count+=1
print('The number of nobita numbers not more than a 100 is {}'.format(count))
for num in nobita:
    print(num)
