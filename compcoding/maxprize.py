def getnum(n):
    i,given=1,0
    prizes=[]
    while n>0:
        if i<=n:
            n-=i
            prizes.append(i)
        else:
            prizes[-1]+=n
            break
        i+=1

    return i-1,prizes

print('This programs helps in finding the max number of kids to distribute candy to, given each of them have a different number')
n=int(input('Enter how many candy you have: '))
i,prizes=getnum(n)
print(i)
for j in prizes:
    print(j,end=' ')
