a=list(map(int,input().split()))
b=list(map(int,input().split()))
ascore=0
bscore=0
for i,thing in enumerate(a):
    if thing>b[i]:
        ascore+=1
    elif thing<b[i]:
        bscore+=1
print(ascore,bscore)
