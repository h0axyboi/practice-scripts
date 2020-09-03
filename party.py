print('This program calculates the minimum number of groups that children at a party can be split into, so that in each group, the children differ in age by atmost 1 year')
print('Enter the ages of the children at the party as space separated integers: ')
ages=list(map(float,input().split()))
curr=last=n=0
while curr<=len(ages)-2:
    last=curr
    while curr<=len(ages)-2 and ages[curr+1]-ages[last]<=1:
        curr+=1
    curr+=1
    n+=1
print(n)
