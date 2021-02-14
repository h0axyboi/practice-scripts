def inorder(t):
    thing=[1]
    answer=[]
    while thing:
        x=thing.pop()
        if x>0:
            if t[x][1]>0:
                thing.append(t[x][1])
            thing.append(-x)
            if t[x][0]>0:
                thing.append(t[x][0])
        else:
            answer.append(-x)
    return answer

def swap(t,k):
    togo=[1]
    depth=1
    while togo:
        togo_=[]
        for i in togo:
            if depth%k==0:
                t[i]=(t[i][1],t[i][0])
            if t[i][0]>0:
                togo_.append(t[i][0])
            if t[i][1]>0:
                togo_.append(t[i][1])
        togo=togo_
        depth+=1

t=[None]+[tuple(map(int,input().split())) for _ in range(int(input()))]
for _ in range(int(input())):
    swap(t,int(input()))
    print(' '.join(str(x) for x in inorder(t)))
