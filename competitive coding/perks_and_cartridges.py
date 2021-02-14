c,d,r,p=tuple(map(int,input().split()))
x=0
ans=[]
while(x<=c):
    if(x>=2 and ans[-2]>ans[-1]):
        break
    ans.append((d+r*x)/p if (c-x)>=(d+r*x)/p else (c-x))
    x+=1
print(ans[-2])
