def moneychange(n):
    arr=[0]
    coins=[1,3,4]
    mintoadd=None
    for i in range(1,n+1):
        if i-coins[0]>=0:
            mintoadd=arr[i-coins[0]]+1
        for coin in coins:
            if i-coin>=0:
                mintoadd=min(mintoadd,arr[i-coin]+1)
        arr.append(mintoadd)
    return arr[-1]
n=int(input())
print(moneychange(n))
