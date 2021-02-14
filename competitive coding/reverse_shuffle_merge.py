import sys
sys.setrecursionlimit(10**6)
def do_the_thing(pure,d,word):
    if len(pure)==0 or len(word)==0:
        return
    global final
    global n
    for thing in pure:
        ind=word.index(thing)
        gachi={}
        for blip in word[ind:]:
            
            gachi[blip]=gachi.get(blip,0)+1
        ok=0
        for blip in d:
            if gachi.get(blip,0)<d[blip]//2:
                ok=1
        if ok==0:
            break
    final+=thing
    if len(final)>=n//2:
        return
    d[thing]-=2
    if d[thing]==0:
        del d[thing]
    pure.remove(thing)
    word=word[ind+1:]
    do_the_thing(pure,d,word)


if __name__ == '__main__':
    s=input()
    n=len(s)
    d={}
    pure=[]
    for thing in s:
        d[thing]=d.get(thing,0)+1
    for thing in d:
        for i in range(d[thing]//2):
            pure.append(thing)
    pure.sort()
    s=s[::-1]
    final=''
    do_the_thing(pure,d,s)
    print(final)
