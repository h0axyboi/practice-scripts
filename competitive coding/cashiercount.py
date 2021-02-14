def cashiercount(n):
    total=i=count=0
    coins=[10,5,1]
    while total<n:
        while n-total>=coins[i] and total<n:
            total+=coins[i]
            count+=1
        i+=1
    return count

print('This programs counts the minimum number of coins of denomination 10,5 and 1 needed to get to a particular natural number number n.')
n=int(input('Enter n:'))
print(cashiercount(n))
