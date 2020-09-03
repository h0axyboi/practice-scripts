def getrevenue(n,money,click):
    rev=0
    while len(click)>0:
        maxc=click.index(max(click))
        maxm=money.index(max(money))
        rev+=click[maxc]*money[maxm]
        del click[maxc]
        del money[maxm]
    return rev

print('This program calculates the max revenue that can be generated on a website with information about money per clicks and clicks per day')
n=int(input('Enter the number of slots:'))
money=list(map(int,input('Enter the profit per click on the ith ad as space separated integers:').split()))
click=list(map(int,input('Enter the clicks per day on the ith slot as space separated integers:').split()))
print(getrevenue(n,money,click))
