def getmajfast(arr):
    freqarr={}
    for thing in arr:
        freqarr[thing]=freqarr.get(thing,0)+1
    dict(map(reversed,freqarr.items())).get(max(freqarr.values()))
    return dict(map(reversed,freqarr.items())).get(max(freqarr.values())),max(freqarr.values())

n=int(input())
arr=list(input().split())
thing,freq=getmajfast(arr)
if freq>n/2:
    print(thing)
else:
    print(0)
