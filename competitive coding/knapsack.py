print('Enter the capacity of the knapsack: ')
W=int(input())
print('Enter the weights of the items in order: ')
w=list(map(int,input().split()))
print('Enter the values of the items in order: ')
v=list(map(int,input().split()))
i,d=0,[]
for i in range(len(w)):
    d.append(v[i]/w[i])
value=0
#print(d)
while W>0:
    #print(W)
    maxi=d.index(max(d))
    #print(w[maxi])
    if w[maxi]<=W:
        W-=w[maxi]
        value+=v[maxi]
        #print(value)
    else:
        value+=d[maxi]*W
        W=0
        #print(value)
    del d[maxi]
    del v[maxi]
    del w[maxi]
print(value)
