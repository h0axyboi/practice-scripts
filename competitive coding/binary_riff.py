n=int(input())
a,b,c=1,(n+1)//2,n
while True:
    print(b)
    direction=input()
    if direction=='up':
        space=b
        b=(b+c+1)//2
        a=space
    else:
        space=b
        b=(b+a-1)//2
        c=space
