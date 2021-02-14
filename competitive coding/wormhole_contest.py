import bisect

def findstart(num):
    pos=bisect.bisect(entries,num)
    if pos==0:
        return -1
    else:
        return entries[pos-1]

def findend(num):
    pos=bisect.bisect_left(exits,num)
    if pos>=y:
        return -1
    else:
        return exits[pos]

n,x,y=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int, input().split())))
entries=list(map(int, input().split()))
exits=list(map(int, input().split()))
entries.sort()
exits.sort()
mini=10**7
for entry,exit in arr:
    entry_time=findstart(entry)
    exit_time=findend(exit)
    if entry_time!=-1 and exit_time!=-1:
        mini=min(mini,exit_time-entry_time+1)
    else:
        continue
print(mini)
