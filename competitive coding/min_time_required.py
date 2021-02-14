def done(machines,day):
    count=0
    for thing in machines:
        count+=day//thing
    return count

def get_min_time(goal,machines,l,r):
    m=(l+r)//2
    if done(machines,m)>=goal:
        if done(machines,m-1)<goal:
            return m
        else:
            return get_min_time(goal,machines,l,m)
    else:
        if(done(machines,m+1)>=goal):
            return m+1
        else:
            return get_min_time(goal,machines,m+1,r)

n,goal=tuple(map(int,input().split()))
machines=list(map(int,input().split()))
l=min(machines)*((goal//n)+1)
r=max(machines)*((goal//n)+1)
print(get_min_time(goal,machines,l,r))
