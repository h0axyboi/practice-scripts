t=int(input())
for _ in range(t):
    h,p=map(int,input().split())
    while p>0 and h>0:
        h=h-p
        p=p//2
    if h<=0:
        print(1)
    else:
        print(0)
