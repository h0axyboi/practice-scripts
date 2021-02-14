def facto(n):
    if n<0:
        return 'Enter a number greater than or equal to zero'
    if n==0:
        return 1
    return(n*facto(n-1))

n=int(input())
print(facto(n))


hh,mm
m=6*mm
h=30*hh + 0.5*m
min(abs(h-m),360-(abs(h-m)))
