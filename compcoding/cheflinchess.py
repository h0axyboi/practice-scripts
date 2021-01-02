t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    moves,owners=[],[]
    isthere=0
    for num in arr:
        if k%num==0:
            moves.append(k//num)
            owners.append(num)
            isthere=1
    if isthere==1:
        print(owners[moves.index(min(moves))])
    else:
        print(-1)
