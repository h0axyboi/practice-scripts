if __name__=='__main__':
    n,k=map(int,input().split())
    imp=[]
    notimp=[]
    for _ in range(n):
        a,b=map(int,input().split())
        if b==1:
            imp.append(a)
        else:
            notimp.append(a)
    imp.sort(reverse=True)
    notimp.sort(reverse=True)
    lost,luck=0,0
    for thing in notimp:
        luck+=thing
    for thing in imp:
        if lost<k:
            luck+=thing
            lost+=1
            continue
        luck-=thing
    print(luck)
