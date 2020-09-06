import math

def brute(p):
    mini=math.sqrt((p[0][0]-p[1][0])**2 +
                   (p[0][1]-p[1][1])**2)
    for i in range(len(p)-1):
        for j in range(i+1,len(p)):
            x=math.sqrt((p[0][0]-p[1][0])**2 +
                        (p[0][1]-p[1][1])**2)
            if x<mini:
                mini=x
    return mini

def minstrip(strip):
    if len(strip)<2:
        return 2000000000.0
    mini=brute([strip[0],strip[1]])
    for i in range(len(strip)-1):
        for j in range(i+1,min(len(strip),i+8)):
            x=brute([strip[i],strip[j]])
            if x<mini:
                mini=x
    return mini

def mind(arr,n):
    if len(arr)<=1:
        return 2000000000.0
    if len(arr)<=3:
        return brute(arr)
    d1=mind(arr[:n//2],len(arr[:n//2]))
    d2=mind(arr[n//2:],len(arr[n//2:]))
    d=min(d1,d2)
    mid=arr[n//2][0]
    strip=[]
    for thing in arr:
        if abs(thing[0]-arr[n//2][0])<=d:
            strip.append(thing)
    d3=minstrip(strip)
    return min(d,d3)

n=int(input())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))
arr.sort(key = lambda x:x[1])
print(mind(arr,n))
